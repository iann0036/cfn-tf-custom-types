# TF::Kubernetes::Ingress PathDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backenddefinition.md">BackendDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backenddefinition.md">BackendDefinition</a></i>
</pre>

## Properties

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backenddefinition.md">BackendDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

