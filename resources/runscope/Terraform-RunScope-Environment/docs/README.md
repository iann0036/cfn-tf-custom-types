# Terraform::RunScope::Environment

CloudFormation equivalent of runscope_environment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RunScope::Environment",
    "Properties" : {
        "<a href="#bucketid" title="BucketId">BucketId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#initialvariables" title="InitialVariables">InitialVariables</a>" : <i>[ <a href="initialvariables.md">InitialVariables</a>, ... ]</i>,
        "<a href="#integrations" title="Integrations">Integrations</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preservecookies" title="PreserveCookies">PreserveCookies</a>" : <i>Boolean</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#retryonfailure" title="RetryOnFailure">RetryOnFailure</a>" : <i>Boolean</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#testid" title="TestId">TestId</a>" : <i>String</i>,
        "<a href="#verifyssl" title="VerifySsl">VerifySsl</a>" : <i>Boolean</i>,
        "<a href="#webhooks" title="Webhooks">Webhooks</a>" : <i>[ String, ... ]</i>,
        "<a href="#emails" title="Emails">Emails</a>" : <i>[ <a href="emails.md">Emails</a>, ... ]</i>,
        "<a href="#remoteagents" title="RemoteAgents">RemoteAgents</a>" : <i>[ <a href="remoteagents.md">RemoteAgents</a>, ... ]</i>,
        "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ <a href="recipients.md">Recipients</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RunScope::Environment
Properties:
    <a href="#bucketid" title="BucketId">BucketId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#initialvariables" title="InitialVariables">InitialVariables</a>: <i>
      - <a href="initialvariables.md">InitialVariables</a></i>
    <a href="#integrations" title="Integrations">Integrations</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preservecookies" title="PreserveCookies">PreserveCookies</a>: <i>Boolean</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#retryonfailure" title="RetryOnFailure">RetryOnFailure</a>: <i>Boolean</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#testid" title="TestId">TestId</a>: <i>String</i>
    <a href="#verifyssl" title="VerifySsl">VerifySsl</a>: <i>Boolean</i>
    <a href="#webhooks" title="Webhooks">Webhooks</a>: <i>
      - String</i>
    <a href="#emails" title="Emails">Emails</a>: <i>
      - <a href="emails.md">Emails</a></i>
    <a href="#remoteagents" title="RemoteAgents">RemoteAgents</a>: <i>
      - <a href="remoteagents.md">RemoteAgents</a></i>
    <a href="#recipients" title="Recipients">Recipients</a>: <i>
      - <a href="recipients.md">Recipients</a></i>
</pre>

## Properties

#### BucketId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialVariables

_Required_: No

_Type_: List of <a href="initialvariables.md">InitialVariables</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Integrations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveCookies

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOnFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifySsl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhooks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Emails

_Required_: No

_Type_: List of <a href="emails.md">Emails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAgents

_Required_: No

_Type_: List of <a href="remoteagents.md">RemoteAgents</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: No

_Type_: List of <a href="recipients.md">Recipients</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

