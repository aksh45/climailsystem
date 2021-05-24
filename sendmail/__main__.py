import click
import sendmail as sm
@click.group()
def main():
    pass
@click.command(name="mdetails")
def umdetails():
    click.echo(sm.usermessagedetails())
@click.command()
def udetails():
    click.echo(sm.userdetails())
@click.command()
def deleteapicreds():
    sm.deleteapicreds()
    click.echo("deleted successfully")
@click.command()
def relogin():
    sm.login()
    click.echo("success")
@click.command()
@click.argument('email_id_of_sender')
@click.argument('Subject')
@click.argument('mssg')
def sendmessage(email_id_of_sender,subject,mssg):
    click.echo("Sending Email")
    sm.sendmessage(email_id_of_sender,subject,mssg)
@click.command()
@click.argument('email_id')
@click.argument('subject')
@click.argument('mssg')
@click.argument('file_path')
def sendmessage_attach(email_id,subject,mssg,file_path):
    click.echo('Sending Email')
    sm.sendmessage_attach(email_id,subject,mssg,file_path)
@click.command()
def getlabels():
    data = sm.GetLabels()
    l = [[x['id'],x['name']] for x in data['labels']]
    printf(l,['Id','Name'])
@click.command()
@click.argument('email_adrss')
@click.argument('subject')
@click.argument('htmlfile',required = False)
@click.argument('html',required = False)
@click.argument('text',required = False)
def sendhtml(email_adrss,subject,html_file = None,html = None,text = None):
    if html_file:
        htm = ""
        with open(html_file,'r+') as fl:
            for x in fl:
                htm += x
        sm.sendhtmlmssg(email_adrss,subject,htm,text)
    else:
        sm.sendhtmlmssg(email_adrss,subject,html,text)
@click.command()
@click.argument('labelid',required = False)
@click.argument('pagetoken',required = False)
@click.argument('displaycount',required = False)
def get_mails(labelid,pagetoken,displaycount):
    if labelid == None:
        labelid = 'INBOX'
    if displaycount == None:
        displaycount = 10
    mails = sm.get_messages_info(labelid = labelid,pagetoken = pagetoken,displaycount = displaycount)
    headings = ['Subject','From','Time','Message Id']
    printf(mails['messages'],headings)

def printf(li,headings):
    count = 0

    for x in li:
        count += 1
        click.echo(f"{count}.")
        index = 0

        for i in x:
            click.echo(f"{headings[index]}: {i}")
            index += 1
        click.echo()

@click.command()
@click.argument('mssgid')
def getcompletemail(mssgid):
    mssg = sm.get_message(mssgid)
    click.echo(mssg)
        

main.add_command(sendmessage)
main.add_command(sendmessage_attach)
main.add_command(relogin)
main.add_command(deleteapicreds)
main.add_command(udetails)
main.add_command(umdetails)
main.add_command(sendhtml)
main.add_command(getlabels)
main.add_command(get_mails)
main.add_command(getcompletemail)
main()
