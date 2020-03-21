# Terraform::Google::MonitoringUptimeCheckConfig

This message configures which resources and services to monitor for availability.


To get more information about UptimeCheckConfig, see:

* [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/monitoring/uptime-checks/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=uptime_check_config_http&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::MonitoringUptimeCheckConfig",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#isinternal" title="IsInternal">IsInternal</a>" : <i>Boolean</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#selectedregions" title="SelectedRegions">SelectedRegions</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
        "<a href="#contentmatchers" title="ContentMatchers">ContentMatchers</a>" : <i>[ <a href="contentmatchers.md">ContentMatchers</a>, ... ]</i>,
        "<a href="#httpcheck" title="HttpCheck">HttpCheck</a>" : <i>[ <a href="httpcheck.md">HttpCheck</a>, ... ]</i>,
        "<a href="#internalcheckers" title="InternalCheckers">InternalCheckers</a>" : <i>[ <a href="internalcheckers.md">InternalCheckers</a>, ... ]</i>,
        "<a href="#monitoredresource" title="MonitoredResource">MonitoredResource</a>" : <i>[ <a href="monitoredresource.md">MonitoredResource</a>, ... ]</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>[ <a href="resourcegroup.md">ResourceGroup</a>, ... ]</i>,
        "<a href="#tcpcheck" title="TcpCheck">TcpCheck</a>" : <i>[ <a href="tcpcheck.md">TcpCheck</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#authinfo" title="AuthInfo">AuthInfo</a>" : <i>[ <a href="authinfo.md">AuthInfo</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::MonitoringUptimeCheckConfig
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#isinternal" title="IsInternal">IsInternal</a>: <i>Boolean</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#selectedregions" title="SelectedRegions">SelectedRegions</a>: <i>
      - String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
    <a href="#contentmatchers" title="ContentMatchers">ContentMatchers</a>: <i>
      - <a href="contentmatchers.md">ContentMatchers</a></i>
    <a href="#httpcheck" title="HttpCheck">HttpCheck</a>: <i>
      - <a href="httpcheck.md">HttpCheck</a></i>
    <a href="#internalcheckers" title="InternalCheckers">InternalCheckers</a>: <i>
      - <a href="internalcheckers.md">InternalCheckers</a></i>
    <a href="#monitoredresource" title="MonitoredResource">MonitoredResource</a>: <i>
      - <a href="monitoredresource.md">MonitoredResource</a></i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>
      - <a href="resourcegroup.md">ResourceGroup</a></i>
    <a href="#tcpcheck" title="TcpCheck">TcpCheck</a>: <i>
      - <a href="tcpcheck.md">TcpCheck</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#authinfo" title="AuthInfo">AuthInfo</a>: <i>
      - <a href="authinfo.md">AuthInfo</a></i>
</pre>

## Properties

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsInternal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

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

_Type_: List of <a href="contentmatchers.md">ContentMatchers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCheck

_Required_: No

_Type_: List of <a href="httpcheck.md">HttpCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalCheckers

_Required_: No

_Type_: List of <a href="internalcheckers.md">InternalCheckers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoredResource

_Required_: No

_Type_: List of <a href="monitoredresource.md">MonitoredResource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: List of <a href="resourcegroup.md">ResourceGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpCheck

_Required_: No

_Type_: List of <a href="tcpcheck.md">TcpCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthInfo

_Required_: No

_Type_: List of <a href="authinfo.md">AuthInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Name

Returns the <code>Name</code> value.

#### UptimeCheckId

Returns the <code>UptimeCheckId</code> value.

