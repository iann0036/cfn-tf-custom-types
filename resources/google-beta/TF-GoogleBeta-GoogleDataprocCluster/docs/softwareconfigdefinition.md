# TF::GoogleBeta::GoogleDataprocCluster SoftwareConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imageversion" title="ImageVersion">ImageVersion</a>" : <i>String</i>,
    "<a href="#optionalcomponents" title="OptionalComponents">OptionalComponents</a>" : <i>[ String, ... ]</i>,
    "<a href="#overrideproperties" title="OverrideProperties">OverrideProperties</a>" : <i>[ <a href="overridepropertiesdefinition.md">OverridePropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageversion" title="ImageVersion">ImageVersion</a>: <i>String</i>
<a href="#optionalcomponents" title="OptionalComponents">OptionalComponents</a>: <i>
      - String</i>
<a href="#overrideproperties" title="OverrideProperties">OverrideProperties</a>: <i>
      - <a href="overridepropertiesdefinition.md">OverridePropertiesDefinition</a></i>
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

_Type_: List of <a href="overridepropertiesdefinition.md">OverridePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

