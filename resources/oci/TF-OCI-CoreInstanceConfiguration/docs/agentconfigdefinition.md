# TF::OCI::CoreInstanceConfiguration AgentConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#areallpluginsdisabled" title="AreAllPluginsDisabled">AreAllPluginsDisabled</a>" : <i>Boolean</i>,
    "<a href="#ismanagementdisabled" title="IsManagementDisabled">IsManagementDisabled</a>" : <i>Boolean</i>,
    "<a href="#ismonitoringdisabled" title="IsMonitoringDisabled">IsMonitoringDisabled</a>" : <i>Boolean</i>,
    "<a href="#pluginsconfig" title="PluginsConfig">PluginsConfig</a>" : <i>[ <a href="pluginsconfigdefinition.md">PluginsConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#areallpluginsdisabled" title="AreAllPluginsDisabled">AreAllPluginsDisabled</a>: <i>Boolean</i>
<a href="#ismanagementdisabled" title="IsManagementDisabled">IsManagementDisabled</a>: <i>Boolean</i>
<a href="#ismonitoringdisabled" title="IsMonitoringDisabled">IsMonitoringDisabled</a>: <i>Boolean</i>
<a href="#pluginsconfig" title="PluginsConfig">PluginsConfig</a>: <i>
      - <a href="pluginsconfigdefinition.md">PluginsConfigDefinition</a></i>
</pre>

## Properties

#### AreAllPluginsDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsManagementDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMonitoringDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PluginsConfig

_Required_: No

_Type_: List of <a href="pluginsconfigdefinition.md">PluginsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

