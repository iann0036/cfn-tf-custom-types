# Terraform::Google::ComputeInterconnectAttachment

CloudFormation equivalent of google_compute_interconnect_attachment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeInterconnectAttachment",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#adminenabled" title="AdminEnabled">AdminEnabled</a>" : <i>Boolean</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>String</i>,
        "<a href="#candidatesubnets" title="CandidateSubnets">CandidateSubnets</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudrouteripaddress" title="CloudRouterIpAddress">CloudRouterIpAddress</a>" : <i>String</i>,
        "<a href="#creationtimestamp" title="CreationTimestamp">CreationTimestamp</a>" : <i>String</i>,
        "<a href="#customerrouteripaddress" title="CustomerRouterIpAddress">CustomerRouterIpAddress</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#edgeavailabilitydomain" title="EdgeAvailabilityDomain">EdgeAvailabilityDomain</a>" : <i>String</i>,
        "<a href="#googlereferenceid" title="GoogleReferenceId">GoogleReferenceId</a>" : <i>String</i>,
        "<a href="#interconnect" title="Interconnect">Interconnect</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pairingkey" title="PairingKey">PairingKey</a>" : <i>String</i>,
        "<a href="#partnerasn" title="PartnerAsn">PartnerAsn</a>" : <i>String</i>,
        "<a href="#privateinterconnectinfo" title="PrivateInterconnectInfo">PrivateInterconnectInfo</a>" : <i>[ &lt;a href=&#34;privateinterconnectinfo.md&#34;&gt;PrivateInterconnectInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>String</i>,
        "<a href="#selflink" title="SelfLink">SelfLink</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vlantag8021q" title="VlanTag8021q">VlanTag8021q</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeInterconnectAttachment
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#adminenabled" title="AdminEnabled">AdminEnabled</a>: <i>Boolean</i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>String</i>
    <a href="#candidatesubnets" title="CandidateSubnets">CandidateSubnets</a>: <i>
      - String</i>
    <a href="#cloudrouteripaddress" title="CloudRouterIpAddress">CloudRouterIpAddress</a>: <i>String</i>
    <a href="#creationtimestamp" title="CreationTimestamp">CreationTimestamp</a>: <i>String</i>
    <a href="#customerrouteripaddress" title="CustomerRouterIpAddress">CustomerRouterIpAddress</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#edgeavailabilitydomain" title="EdgeAvailabilityDomain">EdgeAvailabilityDomain</a>: <i>String</i>
    <a href="#googlereferenceid" title="GoogleReferenceId">GoogleReferenceId</a>: <i>String</i>
    <a href="#interconnect" title="Interconnect">Interconnect</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pairingkey" title="PairingKey">PairingKey</a>: <i>String</i>
    <a href="#partnerasn" title="PartnerAsn">PartnerAsn</a>: <i>String</i>
    <a href="#privateinterconnectinfo" title="PrivateInterconnectInfo">PrivateInterconnectInfo</a>: <i>
      - &lt;a href=&#34;privateinterconnectinfo.md&#34;&gt;PrivateInterconnectInfo&lt;/a&gt;</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>String</i>
    <a href="#selflink" title="SelfLink">SelfLink</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vlantag8021q" title="VlanTag8021q">VlanTag8021q</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CandidateSubnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRouterIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationTimestamp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerRouterIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeAvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleReferenceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interconnect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PairingKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartnerAsn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateInterconnectInfo

_Required_: No

_Type_: List of &lt;a href=&#34;privateinterconnectinfo.md&#34;&gt;PrivateInterconnectInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfLink

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanTag8021q

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudRouterIpAddress

Returns the &lt;code&gt;CloudRouterIpAddress&lt;/code&gt; value.

#### CreationTimestamp

Returns the &lt;code&gt;CreationTimestamp&lt;/code&gt; value.

#### CustomerRouterIpAddress

Returns the &lt;code&gt;CustomerRouterIpAddress&lt;/code&gt; value.

#### GoogleReferenceId

Returns the &lt;code&gt;GoogleReferenceId&lt;/code&gt; value.

#### PairingKey

Returns the &lt;code&gt;PairingKey&lt;/code&gt; value.

#### PartnerAsn

Returns the &lt;code&gt;PartnerAsn&lt;/code&gt; value.

#### PrivateInterconnectInfo

Returns the &lt;code&gt;PrivateInterconnectInfo&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

