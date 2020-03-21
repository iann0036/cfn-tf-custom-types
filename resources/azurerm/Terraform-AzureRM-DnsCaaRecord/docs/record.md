# Terraform::AzureRM::DnsCaaRecord Record

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#flags" title="Flags">Flags</a>: <i>Double</i>
<a href="#tag" title="Tag">Tag</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Flags

Extensible CAA flags, currently only 1 is implemented to set the issuer critical flag.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

A property tag, options are issue, issuewild and iodef.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

A property value such as a registrar domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

