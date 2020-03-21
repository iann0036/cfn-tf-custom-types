# Terraform::Kubernetes::Job Template Spec Volume CephFs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#monitors" title="Monitors">Monitors</a>" : <i>[ String, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#secretfile" title="SecretFile">SecretFile</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ &lt;a href=&#34;template-spec-volume-cephfs-secretref.md&#34;&gt;SecretRef&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#monitors" title="Monitors">Monitors</a>: <i>
      - String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#secretfile" title="SecretFile">SecretFile</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - &lt;a href=&#34;template-spec-volume-cephfs-secretref.md&#34;&gt;SecretRef&lt;/a&gt;</i>
</pre>

## Properties

#### Monitors

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretFile

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-volume-cephfs-secretref.md&#34;&gt;SecretRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

