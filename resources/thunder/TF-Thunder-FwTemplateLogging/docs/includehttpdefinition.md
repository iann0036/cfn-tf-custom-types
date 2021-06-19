# TF::Thunder::FwTemplateLogging IncludeHttpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fileextension" title="FileExtension">FileExtension</a>" : <i>Double</i>,
    "<a href="#l4sessioninfo" title="L4SessionInfo">L4SessionInfo</a>" : <i>Double</i>,
    "<a href="#method" title="Method">Method</a>" : <i>Double</i>,
    "<a href="#requestnumber" title="RequestNumber">RequestNumber</a>" : <i>Double</i>,
    "<a href="#headercfg" title="HeaderCfg">HeaderCfg</a>" : <i>[ <a href="headercfgdefinition.md">HeaderCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fileextension" title="FileExtension">FileExtension</a>: <i>Double</i>
<a href="#l4sessioninfo" title="L4SessionInfo">L4SessionInfo</a>: <i>Double</i>
<a href="#method" title="Method">Method</a>: <i>Double</i>
<a href="#requestnumber" title="RequestNumber">RequestNumber</a>: <i>Double</i>
<a href="#headercfg" title="HeaderCfg">HeaderCfg</a>: <i>
      - <a href="headercfgdefinition.md">HeaderCfgDefinition</a></i>
</pre>

## Properties

#### FileExtension

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionInfo

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderCfg

_Required_: No

_Type_: List of <a href="headercfgdefinition.md">HeaderCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

