# Terraform::Kubernetes::Daemonset Spec Container Lifecycle

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#poststart" title="PostStart">PostStart</a>" : <i>[ <a href="spec-container-lifecycle-poststart.md">PostStart</a>, ... ]</i>,
    "<a href="#prestop" title="PreStop">PreStop</a>" : <i>[ <a href="spec-container-lifecycle-prestop.md">PreStop</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#poststart" title="PostStart">PostStart</a>: <i>
      - <a href="spec-container-lifecycle-poststart.md">PostStart</a></i>
<a href="#prestop" title="PreStop">PreStop</a>: <i>
      - <a href="spec-container-lifecycle-prestop.md">PreStop</a></i>
</pre>

## Properties

#### PostStart

_Required_: No

_Type_: List of <a href="spec-container-lifecycle-poststart.md">PostStart</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStop

_Required_: No

_Type_: List of <a href="spec-container-lifecycle-prestop.md">PreStop</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

