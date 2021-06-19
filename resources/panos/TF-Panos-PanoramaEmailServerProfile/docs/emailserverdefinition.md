# TF::Panos::PanoramaEmailServerProfile EmailServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alsotoemail" title="AlsoToEmail">AlsoToEmail</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#emailgateway" title="EmailGateway">EmailGateway</a>" : <i>String</i>,
    "<a href="#fromemail" title="FromEmail">FromEmail</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#toemail" title="ToEmail">ToEmail</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#alsotoemail" title="AlsoToEmail">AlsoToEmail</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#emailgateway" title="EmailGateway">EmailGateway</a>: <i>String</i>
<a href="#fromemail" title="FromEmail">FromEmail</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#toemail" title="ToEmail">ToEmail</a>: <i>String</i>
</pre>

## Properties

#### AlsoToEmail

Secondary to email address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailGateway

The email server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromEmail

From email address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToEmail

To email address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

