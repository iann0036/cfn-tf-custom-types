# Terraform::Kubernetes::Pod Spec Container Resources

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="spec-container-resources-limits.md">Limits</a>, ... ]</i>,
    "<a href="#requests" title="Requests">Requests</a>" : <i>[ <a href="spec-container-resources-requests.md">Requests</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="spec-container-resources-limits.md">Limits</a></i>
<a href="#requests" title="Requests">Requests</a>: <i>
      - <a href="spec-container-resources-requests.md">Requests</a></i>
</pre>

## Properties

#### Limits

_Required_: No

_Type_: List of <a href="spec-container-resources-limits.md">Limits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Requests

_Required_: No

_Type_: List of <a href="spec-container-resources-requests.md">Requests</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

