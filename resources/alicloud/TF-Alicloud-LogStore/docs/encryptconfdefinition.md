# TF::Alicloud::LogStore EncryptConfDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#encrypttype" title="EncryptType">EncryptType</a>" : <i>String</i>,
    "<a href="#usercmkinfo" title="UserCmkInfo">UserCmkInfo</a>" : <i>[ <a href="usercmkinfodefinition.md">UserCmkInfoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#encrypttype" title="EncryptType">EncryptType</a>: <i>String</i>
<a href="#usercmkinfo" title="UserCmkInfo">UserCmkInfo</a>: <i>
      - <a href="usercmkinfodefinition.md">UserCmkInfoDefinition</a></i>
</pre>

## Properties

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCmkInfo

_Required_: No

_Type_: List of <a href="usercmkinfodefinition.md">UserCmkInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

