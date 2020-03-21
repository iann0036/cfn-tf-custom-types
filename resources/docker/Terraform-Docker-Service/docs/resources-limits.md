# Terraform::Docker::Service Resources Limits

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#memorybytes" title="MemoryBytes">MemoryBytes</a>" : <i>Double</i>,
    "<a href="#nanocpus" title="NanoCpus">NanoCpus</a>" : <i>Double</i>,
    "<a href="#genericresources" title="GenericResources">GenericResources</a>" : <i>[ <a href="resources-limits-genericresources.md">GenericResources</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#memorybytes" title="MemoryBytes">MemoryBytes</a>: <i>Double</i>
<a href="#nanocpus" title="NanoCpus">NanoCpus</a>: <i>Double</i>
<a href="#genericresources" title="GenericResources">GenericResources</a>: <i>
      - <a href="resources-limits-genericresources.md">GenericResources</a></i>
</pre>

## Properties

#### MemoryBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NanoCpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenericResources

_Required_: No

_Type_: List of <a href="resources-limits-genericresources.md">GenericResources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

