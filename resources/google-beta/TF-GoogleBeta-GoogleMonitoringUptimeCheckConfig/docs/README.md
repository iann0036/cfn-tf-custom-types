# TF::GoogleBeta::GoogleMonitoringUptimeCheckConfig

CloudFormation equivalent of google_monitoring_uptime_check_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleMonitoringUptimeCheckConfig",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#selectedregions" title="SelectedRegions">SelectedRegions</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
        "<a href="#contentmatchers" title="ContentMatchers">ContentMatchers</a>" : <i>[ <a href="contentmatchersdefinition.md">ContentMatchersDefinition</a>, ... ]</i>,
        "<a href="#httpcheck" title="HttpCheck">HttpCheck</a>" : <i>[ <a href="httpcheckdefinition.md">HttpCheckDefinition</a>, ... ]</i>,
        "<a href="#monitoredresource" title="MonitoredResource">MonitoredResource</a>" : <i>[ <a href="monitoredresourcedefinition.md">MonitoredResourceDefinition</a>, ... ]</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>[ <a href="resourcegroupdefinition.md">ResourceGroupDefinition</a>, ... ]</i>,
        "<a href="#tcpcheck" title="TcpCheck">TcpCheck</a>" : <i>[ <a href="tcpcheckdefinition.md">TcpCheckDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleMonitoringUptimeCheckConfig
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#selectedregions" title="SelectedRegions">SelectedRegions</a>: <i>
      - String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
    <a href="#contentmatchers" title="ContentMatchers">ContentMatchers</a>: <i>
      - <a href="contentmatchersdefinition.md">ContentMatchersDefinition</a></i>
    <a href="#httpcheck" title="HttpCheck">HttpCheck</a>: <i>
      - <a href="httpcheckdefinition.md">HttpCheckDefinition</a></i>
    <a href="#monitoredresource" title="MonitoredResource">MonitoredResource</a>: <i>
      - <a href="monitoredresourcedefinition.md">MonitoredResourceDefinition</a></i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>
      - <a href="resourcegroupdefinition.md">ResourceGroupDefinition</a></i>
    <a href="#tcpcheck" title="TcpCheck">TcpCheck</a>: <i>
      - <a href="tcpcheckdefinition.md">TcpCheckDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedRegions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentMatchers

_Required_: No

_Type_: List of <a href="contentmatchersdefinition.md">ContentMatchersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCheck

_Required_: No

_Type_: List of <a href="httpcheckdefinition.md">HttpCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoredResource

_Required_: No

_Type_: List of <a href="monitoredresourcedefinition.md">MonitoredResourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: List of <a href="resourcegroupdefinition.md">ResourceGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpCheck

_Required_: No

_Type_: List of <a href="tcpcheckdefinition.md">TcpCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### UptimeCheckId

Returns the <code>UptimeCheckId</code> value.

