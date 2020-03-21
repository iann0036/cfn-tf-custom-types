# Terraform::Kubernetes::Pod Container Env ValueFrom

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>" : <i>[ &lt;a href=&#34;container-env-valuefrom-configmapkeyref.md&#34;&gt;ConfigMapKeyRef&lt;/a&gt;, ... ]</i>,
    "<a href="#fieldref" title="FieldRef">FieldRef</a>" : <i>[ &lt;a href=&#34;container-env-valuefrom-fieldref.md&#34;&gt;FieldRef&lt;/a&gt;, ... ]</i>,
    "<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>" : <i>[ &lt;a href=&#34;container-env-valuefrom-resourcefieldref.md&#34;&gt;ResourceFieldRef&lt;/a&gt;, ... ]</i>,
    "<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>" : <i>[ &lt;a href=&#34;container-env-valuefrom-secretkeyref.md&#34;&gt;SecretKeyRef&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>: <i>
      - &lt;a href=&#34;container-env-valuefrom-configmapkeyref.md&#34;&gt;ConfigMapKeyRef&lt;/a&gt;</i>
<a href="#fieldref" title="FieldRef">FieldRef</a>: <i>
      - &lt;a href=&#34;container-env-valuefrom-fieldref.md&#34;&gt;FieldRef&lt;/a&gt;</i>
<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>: <i>
      - &lt;a href=&#34;container-env-valuefrom-resourcefieldref.md&#34;&gt;ResourceFieldRef&lt;/a&gt;</i>
<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>: <i>
      - &lt;a href=&#34;container-env-valuefrom-secretkeyref.md&#34;&gt;SecretKeyRef&lt;/a&gt;</i>
</pre>

## Properties

#### ConfigMapKeyRef

_Required_: No
_Type_: List of &lt;a href=&#34;container-env-valuefrom-configmapkeyref.md&#34;&gt;ConfigMapKeyRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldRef

_Required_: No
_Type_: List of &lt;a href=&#34;container-env-valuefrom-fieldref.md&#34;&gt;FieldRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFieldRef

_Required_: No
_Type_: List of &lt;a href=&#34;container-env-valuefrom-resourcefieldref.md&#34;&gt;ResourceFieldRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKeyRef

_Required_: No
_Type_: List of &lt;a href=&#34;container-env-valuefrom-secretkeyref.md&#34;&gt;SecretKeyRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

