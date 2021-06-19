# TF::Thunder::RouterBgpRedistribute VipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#onlyflaggedcfg" title="OnlyFlaggedCfg">OnlyFlaggedCfg</a>" : <i>[ <a href="onlyflaggedcfgdefinition.md">OnlyFlaggedCfgDefinition</a>, ... ]</i>,
    "<a href="#onlynotflaggedcfg" title="OnlyNotFlaggedCfg">OnlyNotFlaggedCfg</a>" : <i>[ <a href="onlynotflaggedcfgdefinition.md">OnlyNotFlaggedCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#onlyflaggedcfg" title="OnlyFlaggedCfg">OnlyFlaggedCfg</a>: <i>
      - <a href="onlyflaggedcfgdefinition.md">OnlyFlaggedCfgDefinition</a></i>
<a href="#onlynotflaggedcfg" title="OnlyNotFlaggedCfg">OnlyNotFlaggedCfg</a>: <i>
      - <a href="onlynotflaggedcfgdefinition.md">OnlyNotFlaggedCfgDefinition</a></i>
</pre>

## Properties

#### OnlyFlaggedCfg

_Required_: No

_Type_: List of <a href="onlyflaggedcfgdefinition.md">OnlyFlaggedCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyNotFlaggedCfg

_Required_: No

_Type_: List of <a href="onlynotflaggedcfgdefinition.md">OnlyNotFlaggedCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

