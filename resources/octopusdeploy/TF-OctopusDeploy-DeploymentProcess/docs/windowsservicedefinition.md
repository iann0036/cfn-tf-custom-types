# TF::OctopusDeploy::DeploymentProcess WindowsServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arguments" title="Arguments">Arguments</a>" : <i>String</i>,
    "<a href="#createorupdateservice" title="CreateOrUpdateService">CreateOrUpdateService</a>" : <i>Boolean</i>,
    "<a href="#customaccountname" title="CustomAccountName">CustomAccountName</a>" : <i>String</i>,
    "<a href="#customaccountpassword" title="CustomAccountPassword">CustomAccountPassword</a>" : <i>String</i>,
    "<a href="#dependencies" title="Dependencies">Dependencies</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#executablepath" title="ExecutablePath">ExecutablePath</a>" : <i>String</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    "<a href="#startmode" title="StartMode">StartMode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#arguments" title="Arguments">Arguments</a>: <i>String</i>
<a href="#createorupdateservice" title="CreateOrUpdateService">CreateOrUpdateService</a>: <i>Boolean</i>
<a href="#customaccountname" title="CustomAccountName">CustomAccountName</a>: <i>String</i>
<a href="#customaccountpassword" title="CustomAccountPassword">CustomAccountPassword</a>: <i>String</i>
<a href="#dependencies" title="Dependencies">Dependencies</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#executablepath" title="ExecutablePath">ExecutablePath</a>: <i>String</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
<a href="#startmode" title="StartMode">StartMode</a>: <i>String</i>
</pre>

## Properties

#### Arguments

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOrUpdateService

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAccountPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dependencies

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutablePath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

