# Terraform::Kubernetes::CronJob Spec Container EnvFrom

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>" : <i>[ <a href="spec-container-envfrom-configmapref.md">ConfigMapRef</a>, ... ]</i>,
    "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ <a href="spec-container-envfrom-secretref.md">SecretRef</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>: <i>
      - <a href="spec-container-envfrom-configmapref.md">ConfigMapRef</a></i>
<a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - <a href="spec-container-envfrom-secretref.md">SecretRef</a></i>
</pre>

## Properties

#### Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapRef

_Required_: No

_Type_: List of <a href="spec-container-envfrom-configmapref.md">ConfigMapRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of <a href="spec-container-envfrom-secretref.md">SecretRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

