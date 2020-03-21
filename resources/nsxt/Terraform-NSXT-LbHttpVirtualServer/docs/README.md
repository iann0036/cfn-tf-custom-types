# Terraform::NSXT::LbHttpVirtualServer

CloudFormation equivalent of nsxt_lb_http_virtual_server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbHttpVirtualServer",
    "Properties" : {
        "<a href="#accesslogenabled" title="AccessLogEnabled">AccessLogEnabled</a>" : <i>Boolean</i>,
        "<a href="#applicationprofileid" title="ApplicationProfileId">ApplicationProfileId</a>" : <i>String</i>,
        "<a href="#defaultpoolmemberport" title="DefaultPoolMemberPort">DefaultPoolMemberPort</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#maxconcurrentconnections" title="MaxConcurrentConnections">MaxConcurrentConnections</a>" : <i>Double</i>,
        "<a href="#maxnewconnectionrate" title="MaxNewConnectionRate">MaxNewConnectionRate</a>" : <i>Double</i>,
        "<a href="#persistenceprofileid" title="PersistenceProfileId">PersistenceProfileId</a>" : <i>String</i>,
        "<a href="#poolid" title="PoolId">PoolId</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#ruleids" title="RuleIds">RuleIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sorrypoolid" title="SorryPoolId">SorryPoolId</a>" : <i>String</i>,
        "<a href="#clientssl" title="ClientSsl">ClientSsl</a>" : <i>[ &lt;a href=&#34;clientssl.md&#34;&gt;ClientSsl&lt;/a&gt;, ... ]</i>,
        "<a href="#serverssl" title="ServerSsl">ServerSsl</a>" : <i>[ &lt;a href=&#34;serverssl.md&#34;&gt;ServerSsl&lt;/a&gt;, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbHttpVirtualServer
Properties:
    <a href="#accesslogenabled" title="AccessLogEnabled">AccessLogEnabled</a>: <i>Boolean</i>
    <a href="#applicationprofileid" title="ApplicationProfileId">ApplicationProfileId</a>: <i>String</i>
    <a href="#defaultpoolmemberport" title="DefaultPoolMemberPort">DefaultPoolMemberPort</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#maxconcurrentconnections" title="MaxConcurrentConnections">MaxConcurrentConnections</a>: <i>Double</i>
    <a href="#maxnewconnectionrate" title="MaxNewConnectionRate">MaxNewConnectionRate</a>: <i>Double</i>
    <a href="#persistenceprofileid" title="PersistenceProfileId">PersistenceProfileId</a>: <i>String</i>
    <a href="#poolid" title="PoolId">PoolId</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#ruleids" title="RuleIds">RuleIds</a>: <i>
      - String</i>
    <a href="#sorrypoolid" title="SorryPoolId">SorryPoolId</a>: <i>String</i>
    <a href="#clientssl" title="ClientSsl">ClientSsl</a>: <i>
      - &lt;a href=&#34;clientssl.md&#34;&gt;ClientSsl&lt;/a&gt;</i>
    <a href="#serverssl" title="ServerSsl">ServerSsl</a>: <i>
      - &lt;a href=&#34;serverssl.md&#34;&gt;ServerSsl&lt;/a&gt;</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;</i>
</pre>

## Properties

#### AccessLogEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationProfileId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPoolMemberPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentConnections

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNewConnectionRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceProfileId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SorryPoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSsl

_Required_: No

_Type_: List of &lt;a href=&#34;clientssl.md&#34;&gt;ClientSsl&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSsl

_Required_: No

_Type_: List of &lt;a href=&#34;serverssl.md&#34;&gt;ServerSsl&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.

