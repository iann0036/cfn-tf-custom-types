# TF::AVI::Cloud DockerRegistrySeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#private" title="Private">Private</a>" : <i>Boolean</i>,
    "<a href="#registry" title="Registry">Registry</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#oshiftregistry" title="OshiftRegistry">OshiftRegistry</a>" : <i>[ <a href="oshiftregistrydefinition.md">OshiftRegistryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#private" title="Private">Private</a>: <i>Boolean</i>
<a href="#registry" title="Registry">Registry</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#oshiftregistry" title="OshiftRegistry">OshiftRegistry</a>: <i>
      - <a href="oshiftregistrydefinition.md">OshiftRegistryDefinition</a></i>
</pre>

## Properties

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Private

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Registry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OshiftRegistry

_Required_: No

_Type_: List of <a href="oshiftregistrydefinition.md">OshiftRegistryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

