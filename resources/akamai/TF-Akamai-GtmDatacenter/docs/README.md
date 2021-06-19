# TF::Akamai::GtmDatacenter

Use the `akamai_gtm_datacenter` resource to create, configure, and import a GTM data center. A GTM data center represents a customer data center and is also known as a traffic target, a location containing many servers GTM can direct traffic to. 

GTM uses data centers to scale load balancing. For example, you might have data centers in both New York and Amsterdam and want to balance load between them. You can configure GTM to send US users to the New York data center and European users to the data center in Amsterdam. 

~> **Note** Import requires an ID with this format: `existing_domain_name`:`existing_datacenter_id`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::GtmDatacenter",
    "Properties" : {
        "<a href="#city" title="City">City</a>" : <i>String</i>,
        "<a href="#cloneof" title="CloneOf">CloneOf</a>" : <i>Double</i>,
        "<a href="#cloudserverhostheaderoverride" title="CloudServerHostHeaderOverride">CloudServerHostHeaderOverride</a>" : <i>Boolean</i>,
        "<a href="#cloudservertargeting" title="CloudServerTargeting">CloudServerTargeting</a>" : <i>Boolean</i>,
        "<a href="#continent" title="Continent">Continent</a>" : <i>String</i>,
        "<a href="#country" title="Country">Country</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#latitude" title="Latitude">Latitude</a>" : <i>Double</i>,
        "<a href="#longitude" title="Longitude">Longitude</a>" : <i>Double</i>,
        "<a href="#nickname" title="Nickname">Nickname</a>" : <i>String</i>,
        "<a href="#stateorprovince" title="StateOrProvince">StateOrProvince</a>" : <i>String</i>,
        "<a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>" : <i>Boolean</i>,
        "<a href="#defaultloadobject" title="DefaultLoadObject">DefaultLoadObject</a>" : <i>[ <a href="defaultloadobjectdefinition.md">DefaultLoadObjectDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::GtmDatacenter
Properties:
    <a href="#city" title="City">City</a>: <i>String</i>
    <a href="#cloneof" title="CloneOf">CloneOf</a>: <i>Double</i>
    <a href="#cloudserverhostheaderoverride" title="CloudServerHostHeaderOverride">CloudServerHostHeaderOverride</a>: <i>Boolean</i>
    <a href="#cloudservertargeting" title="CloudServerTargeting">CloudServerTargeting</a>: <i>Boolean</i>
    <a href="#continent" title="Continent">Continent</a>: <i>String</i>
    <a href="#country" title="Country">Country</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#latitude" title="Latitude">Latitude</a>: <i>Double</i>
    <a href="#longitude" title="Longitude">Longitude</a>: <i>Double</i>
    <a href="#nickname" title="Nickname">Nickname</a>: <i>String</i>
    <a href="#stateorprovince" title="StateOrProvince">StateOrProvince</a>: <i>String</i>
    <a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>: <i>Boolean</i>
    <a href="#defaultloadobject" title="DefaultLoadObject">DefaultLoadObject</a>: <i>
      - <a href="defaultloadobjectdefinition.md">DefaultLoadObjectDefinition</a></i>
</pre>

## Properties

#### City

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloneOf

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudServerHostHeaderOverride

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudServerTargeting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Continent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Latitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Longitude

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nickname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateOrProvince

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitOnComplete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLoadObject

_Required_: No

_Type_: List of <a href="defaultloadobjectdefinition.md">DefaultLoadObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DatacenterId

Returns the <code>DatacenterId</code> value.

#### Id

Returns the <code>Id</code> value.

#### PingInterval

Returns the <code>PingInterval</code> value.

#### PingPacketSize

Returns the <code>PingPacketSize</code> value.

#### ScorePenalty

Returns the <code>ScorePenalty</code> value.

#### ServermonitorLivenessCount

Returns the <code>ServermonitorLivenessCount</code> value.

#### ServermonitorLoadCount

Returns the <code>ServermonitorLoadCount</code> value.

#### ServermonitorPool

Returns the <code>ServermonitorPool</code> value.

#### Virtual

Returns the <code>Virtual</code> value.

