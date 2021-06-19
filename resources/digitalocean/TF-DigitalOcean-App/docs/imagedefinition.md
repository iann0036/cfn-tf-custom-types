# TF::DigitalOcean::App ImageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#registry" title="Registry">Registry</a>" : <i>String</i>,
    "<a href="#registrytype" title="RegistryType">RegistryType</a>" : <i>String</i>,
    "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#registry" title="Registry">Registry</a>: <i>String</i>
<a href="#registrytype" title="RegistryType">RegistryType</a>: <i>String</i>
<a href="#repository" title="Repository">Repository</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>String</i>
</pre>

## Properties

#### Registry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

