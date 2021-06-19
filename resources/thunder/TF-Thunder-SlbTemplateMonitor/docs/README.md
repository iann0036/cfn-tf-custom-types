# TF::Thunder::SlbTemplateMonitor

`thunder_slb_template_monitor` Provides details about thunder slb template monitor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateMonitor",
    "Properties" : {
        "<a href="#id2" title="Id2">Id2</a>" : <i>Double</i>,
        "<a href="#monitorrelation" title="MonitorRelation">MonitorRelation</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#clearcfg" title="ClearCfg">ClearCfg</a>" : <i>[ <a href="clearcfgdefinition.md">ClearCfgDefinition</a>, ... ]</i>,
        "<a href="#linkdisablecfg" title="LinkDisableCfg">LinkDisableCfg</a>" : <i>[ <a href="linkdisablecfgdefinition.md">LinkDisableCfgDefinition</a>, ... ]</i>,
        "<a href="#linkdowncfg" title="LinkDownCfg">LinkDownCfg</a>" : <i>[ <a href="linkdowncfgdefinition.md">LinkDownCfgDefinition</a>, ... ]</i>,
        "<a href="#linkenablecfg" title="LinkEnableCfg">LinkEnableCfg</a>" : <i>[ <a href="linkenablecfgdefinition.md">LinkEnableCfgDefinition</a>, ... ]</i>,
        "<a href="#linkupcfg" title="LinkUpCfg">LinkUpCfg</a>" : <i>[ <a href="linkupcfgdefinition.md">LinkUpCfgDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateMonitor
Properties:
    <a href="#id2" title="Id2">Id2</a>: <i>Double</i>
    <a href="#monitorrelation" title="MonitorRelation">MonitorRelation</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#clearcfg" title="ClearCfg">ClearCfg</a>: <i>
      - <a href="clearcfgdefinition.md">ClearCfgDefinition</a></i>
    <a href="#linkdisablecfg" title="LinkDisableCfg">LinkDisableCfg</a>: <i>
      - <a href="linkdisablecfgdefinition.md">LinkDisableCfgDefinition</a></i>
    <a href="#linkdowncfg" title="LinkDownCfg">LinkDownCfg</a>: <i>
      - <a href="linkdowncfgdefinition.md">LinkDownCfgDefinition</a></i>
    <a href="#linkenablecfg" title="LinkEnableCfg">LinkEnableCfg</a>: <i>
      - <a href="linkenablecfgdefinition.md">LinkEnableCfgDefinition</a></i>
    <a href="#linkupcfg" title="LinkUpCfg">LinkUpCfg</a>: <i>
      - <a href="linkupcfgdefinition.md">LinkUpCfgDefinition</a></i>
</pre>

## Properties

#### Id2

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorRelation

‘monitor-and’: Configures the monitors in current template to work with AND logic; ‘monitor-or’: Configures the monitors in current template to work with OR logic;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearCfg

_Required_: No

_Type_: List of <a href="clearcfgdefinition.md">ClearCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkDisableCfg

_Required_: No

_Type_: List of <a href="linkdisablecfgdefinition.md">LinkDisableCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkDownCfg

_Required_: No

_Type_: List of <a href="linkdowncfgdefinition.md">LinkDownCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkEnableCfg

_Required_: No

_Type_: List of <a href="linkenablecfgdefinition.md">LinkEnableCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkUpCfg

_Required_: No

_Type_: List of <a href="linkupcfgdefinition.md">LinkUpCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Monitor template ID Number.

