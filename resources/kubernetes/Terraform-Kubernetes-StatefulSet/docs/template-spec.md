# Terraform::Kubernetes::StatefulSet Template Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessmodes" title="AccessModes">AccessModes</a>" : <i>[ String, ... ]</i>,
    "<a href="#storageclassname" title="StorageClassName">StorageClassName</a>" : <i>String</i>,
    "<a href="#volumename" title="VolumeName">VolumeName</a>" : <i>String</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;template-spec-resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>[ &lt;a href=&#34;template-spec-selector.md&#34;&gt;Selector&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accessmodes" title="AccessModes">AccessModes</a>: <i>
      - String</i>
<a href="#storageclassname" title="StorageClassName">StorageClassName</a>: <i>String</i>
<a href="#volumename" title="VolumeName">VolumeName</a>: <i>String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;template-spec-resources.md&#34;&gt;Resources&lt;/a&gt;</i>
<a href="#selector" title="Selector">Selector</a>: <i>
      - &lt;a href=&#34;template-spec-selector.md&#34;&gt;Selector&lt;/a&gt;</i>
</pre>

## Properties

#### AccessModes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClassName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-selector.md&#34;&gt;Selector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

