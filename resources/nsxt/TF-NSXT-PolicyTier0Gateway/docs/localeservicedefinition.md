# TF::NSXT::PolicyTier0Gateway LocaleServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#edgeclusterpath" title="EdgeClusterPath">EdgeClusterPath</a>" : <i>String</i>,
    "<a href="#preferrededgepaths" title="PreferredEdgePaths">PreferredEdgePaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#redistributionconfig" title="RedistributionConfig">RedistributionConfig</a>" : <i>[ <a href="redistributionconfigdefinition.md">RedistributionConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#edgeclusterpath" title="EdgeClusterPath">EdgeClusterPath</a>: <i>String</i>
<a href="#preferrededgepaths" title="PreferredEdgePaths">PreferredEdgePaths</a>: <i>
      - String</i>
<a href="#redistributionconfig" title="RedistributionConfig">RedistributionConfig</a>: <i>
      - <a href="redistributionconfigdefinition.md">RedistributionConfigDefinition</a></i>
</pre>

## Properties

#### EdgeClusterPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredEdgePaths

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributionConfig

_Required_: No

_Type_: List of <a href="redistributionconfigdefinition.md">RedistributionConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

