# Terraform::Panos::PanoramaLogForwardingProfile MatchList

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#emailserverprofiles" title="EmailServerProfiles">EmailServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#httpserverprofiles" title="HttpServerProfiles">HttpServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sendtopanorama" title="SendToPanorama">SendToPanorama</a>" : <i>Boolean</i>,
    "<a href="#snmptrapserverprofiles" title="SnmptrapServerProfiles">SnmptrapServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#syslogserverprofiles" title="SyslogServerProfiles">SyslogServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;matchlist-action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#emailserverprofiles" title="EmailServerProfiles">EmailServerProfiles</a>: <i>
      - String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#httpserverprofiles" title="HttpServerProfiles">HttpServerProfiles</a>: <i>
      - String</i>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sendtopanorama" title="SendToPanorama">SendToPanorama</a>: <i>Boolean</i>
<a href="#snmptrapserverprofiles" title="SnmptrapServerProfiles">SnmptrapServerProfiles</a>: <i>
      - String</i>
<a href="#syslogserverprofiles" title="SyslogServerProfiles">SyslogServerProfiles</a>: <i>
      - String</i>
<a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;matchlist-action.md&#34;&gt;Action&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailServerProfiles

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServerProfiles

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendToPanorama

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmptrapServerProfiles

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogServerProfiles

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No
_Type_: List of &lt;a href=&#34;matchlist-action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

