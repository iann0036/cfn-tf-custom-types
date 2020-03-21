# Terraform::Google::DataprocCluster SoftwareConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imageversion" title="ImageVersion">ImageVersion</a>" : <i>String</i>,
    "<a href="#optionalcomponents" title="OptionalComponents">OptionalComponents</a>" : <i>[ String, ... ]</i>,
    "<a href="#overrideproperties" title="OverrideProperties">OverrideProperties</a>" : <i>[ &lt;a href=&#34;softwareconfig-overrideproperties.md&#34;&gt;OverrideProperties&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageversion" title="ImageVersion">ImageVersion</a>: <i>String</i>
<a href="#optionalcomponents" title="OptionalComponents">OptionalComponents</a>: <i>
      - String</i>
<a href="#overrideproperties" title="OverrideProperties">OverrideProperties</a>: <i>
      - &lt;a href=&#34;softwareconfig-overrideproperties.md&#34;&gt;OverrideProperties&lt;/a&gt;</i>
</pre>

## Properties

#### ImageVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalComponents

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideProperties

_Required_: No
_Type_: List of &lt;a href=&#34;softwareconfig-overrideproperties.md&#34;&gt;OverrideProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

