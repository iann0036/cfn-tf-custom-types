# TF::GoogleBeta::GoogleBigqueryConnection CloudSqlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#database" title="Database">Database</a>" : <i>String</i>,
    "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#credential" title="Credential">Credential</a>" : <i>[ <a href="credentialdefinition.md">CredentialDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#database" title="Database">Database</a>: <i>String</i>
<a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#credential" title="Credential">Credential</a>: <i>
      - <a href="credentialdefinition.md">CredentialDefinition</a></i>
</pre>

## Properties

#### Database

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credential

_Required_: No

_Type_: List of <a href="credentialdefinition.md">CredentialDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

