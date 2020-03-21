# Terraform::Google::MonitoringUptimeCheckConfig

CloudFormation equivalent of google_monitoring_uptime_check_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::MonitoringUptimeCheckConfig",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#isinternal" title="IsInternal">IsInternal</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#selectedregions" title="SelectedRegions">SelectedRegions</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
        "<a href="#uptimecheckid" title="UptimeCheckId">UptimeCheckId</a>" : <i>String</i>,
        "<a href="#contentmatchers" title="ContentMatchers">ContentMatchers</a>" : <i>[ &lt;a href=&#34;contentmatchers.md&#34;&gt;ContentMatchers&lt;/a&gt;, ... ]</i>,
        "<a href="#httpcheck" title="HttpCheck">HttpCheck</a>" : <i>[ &lt;a href=&#34;httpcheck.md&#34;&gt;HttpCheck&lt;/a&gt;, ... ]</i>,
        "<a href="#internalcheckers" title="InternalCheckers">InternalCheckers</a>" : <i>[ &lt;a href=&#34;internalcheckers.md&#34;&gt;InternalCheckers&lt;/a&gt;, ... ]</i>,
        "<a href="#monitoredresource" title="MonitoredResource">MonitoredResource</a>" : <i>[ &lt;a href=&#34;monitoredresource.md&#34;&gt;MonitoredResource&lt;/a&gt;, ... ]</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>[ &lt;a href=&#34;resourcegroup.md&#34;&gt;ResourceGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#tcpcheck" title="TcpCheck">TcpCheck</a>" : <i>[ &lt;a href=&#34;tcpcheck.md&#34;&gt;TcpCheck&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#authinfo" title="AuthInfo">AuthInfo</a>" : <i>[ &lt;a href=&#34;authinfo.md&#34;&gt;AuthInfo&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::MonitoringUptimeCheckConfig
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#isinternal" title="IsInternal">IsInternal</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#selectedregions" title="SelectedRegions">SelectedRegions</a>: <i>
      - String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
    <a href="#uptimecheckid" title="UptimeCheckId">UptimeCheckId</a>: <i>String</i>
    <a href="#contentmatchers" title="ContentMatchers">ContentMatchers</a>: <i>
      - &lt;a href=&#34;contentmatchers.md&#34;&gt;ContentMatchers&lt;/a&gt;</i>
    <a href="#httpcheck" title="HttpCheck">HttpCheck</a>: <i>
      - &lt;a href=&#34;httpcheck.md&#34;&gt;HttpCheck&lt;/a&gt;</i>
    <a href="#internalcheckers" title="InternalCheckers">InternalCheckers</a>: <i>
      - &lt;a href=&#34;internalcheckers.md&#34;&gt;InternalCheckers&lt;/a&gt;</i>
    <a href="#monitoredresource" title="MonitoredResource">MonitoredResource</a>: <i>
      - &lt;a href=&#34;monitoredresource.md&#34;&gt;MonitoredResource&lt;/a&gt;</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>
      - &lt;a href=&#34;resourcegroup.md&#34;&gt;ResourceGroup&lt;/a&gt;</i>
    <a href="#tcpcheck" title="TcpCheck">TcpCheck</a>: <i>
      - &lt;a href=&#34;tcpcheck.md&#34;&gt;TcpCheck&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#authinfo" title="AuthInfo">AuthInfo</a>: <i>
      - &lt;a href=&#34;authinfo.md&#34;&gt;AuthInfo&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsInternal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

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

#### UptimeCheckId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentMatchers

_Required_: No

_Type_: List of &lt;a href=&#34;contentmatchers.md&#34;&gt;ContentMatchers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCheck

_Required_: No

_Type_: List of &lt;a href=&#34;httpcheck.md&#34;&gt;HttpCheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalCheckers

_Required_: No

_Type_: List of &lt;a href=&#34;internalcheckers.md&#34;&gt;InternalCheckers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoredResource

_Required_: No

_Type_: List of &lt;a href=&#34;monitoredresource.md&#34;&gt;MonitoredResource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: List of &lt;a href=&#34;resourcegroup.md&#34;&gt;ResourceGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpCheck

_Required_: No

_Type_: List of &lt;a href=&#34;tcpcheck.md&#34;&gt;TcpCheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthInfo

_Required_: No

_Type_: List of &lt;a href=&#34;authinfo.md&#34;&gt;AuthInfo&lt;/a&gt;

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

Returns the &lt;code&gt;Name&lt;/code&gt; value.

#### UptimeCheckId

Returns the &lt;code&gt;UptimeCheckId&lt;/code&gt; value.

