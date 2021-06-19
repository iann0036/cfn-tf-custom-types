# TF::Gridscale::Storage TemplateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#passwordtype" title="PasswordType">PasswordType</a>" : <i>String</i>,
    "<a href="#sshkeys" title="Sshkeys">Sshkeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#passwordtype" title="PasswordType">PasswordType</a>: <i>String</i>
<a href="#sshkeys" title="Sshkeys">Sshkeys</a>: <i>
      - String</i>
<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>: <i>String</i>
</pre>

## Properties

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sshkeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

