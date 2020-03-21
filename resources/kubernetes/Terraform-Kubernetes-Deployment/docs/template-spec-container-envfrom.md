# Terraform::Kubernetes::Deployment Template Spec Container EnvFrom

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>" : <i>[ &lt;a href=&#34;template-spec-container-envfrom-configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;, ... ]</i>,
    "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ &lt;a href=&#34;template-spec-container-envfrom-secretref.md&#34;&gt;SecretRef&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>: <i>
      - &lt;a href=&#34;template-spec-container-envfrom-configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;</i>
<a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - &lt;a href=&#34;template-spec-container-envfrom-secretref.md&#34;&gt;SecretRef&lt;/a&gt;</i>
</pre>

## Properties

#### Prefix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapRef

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-container-envfrom-configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-container-envfrom-secretref.md&#34;&gt;SecretRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

