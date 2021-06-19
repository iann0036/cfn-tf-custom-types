# TF::Akamai::GtmDomain

Use the `akamai_gtm_domain` resource to create, configure, and import a GTM Domain, which is a basic building block of a traffic management configuration. 

~> **Note** Import requires an ID with this format: `existing_domain_name`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::GtmDomain",
    "Properties" : {
        "<a href="#cnamecoalescingenabled" title="CnameCoalescingEnabled">CnameCoalescingEnabled</a>" : <i>Boolean</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#contract" title="Contract">Contract</a>" : <i>String</i>,
        "<a href="#defaulterrorpenalty" title="DefaultErrorPenalty">DefaultErrorPenalty</a>" : <i>Double</i>,
        "<a href="#defaultsslclientcertificate" title="DefaultSslClientCertificate">DefaultSslClientCertificate</a>" : <i>String</i>,
        "<a href="#defaultsslclientprivatekey" title="DefaultSslClientPrivateKey">DefaultSslClientPrivateKey</a>" : <i>String</i>,
        "<a href="#defaulttimeoutpenalty" title="DefaultTimeoutPenalty">DefaultTimeoutPenalty</a>" : <i>Double</i>,
        "<a href="#emailnotificationlist" title="EmailNotificationList">EmailNotificationList</a>" : <i>[ String, ... ]</i>,
        "<a href="#endusermappingenabled" title="EndUserMappingEnabled">EndUserMappingEnabled</a>" : <i>Boolean</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#loadfeedback" title="LoadFeedback">LoadFeedback</a>" : <i>Boolean</i>,
        "<a href="#loadimbalancepercentage" title="LoadImbalancePercentage">LoadImbalancePercentage</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::GtmDomain
Properties:
    <a href="#cnamecoalescingenabled" title="CnameCoalescingEnabled">CnameCoalescingEnabled</a>: <i>Boolean</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#contract" title="Contract">Contract</a>: <i>String</i>
    <a href="#defaulterrorpenalty" title="DefaultErrorPenalty">DefaultErrorPenalty</a>: <i>Double</i>
    <a href="#defaultsslclientcertificate" title="DefaultSslClientCertificate">DefaultSslClientCertificate</a>: <i>String</i>
    <a href="#defaultsslclientprivatekey" title="DefaultSslClientPrivateKey">DefaultSslClientPrivateKey</a>: <i>String</i>
    <a href="#defaulttimeoutpenalty" title="DefaultTimeoutPenalty">DefaultTimeoutPenalty</a>: <i>Double</i>
    <a href="#emailnotificationlist" title="EmailNotificationList">EmailNotificationList</a>: <i>
      - String</i>
    <a href="#endusermappingenabled" title="EndUserMappingEnabled">EndUserMappingEnabled</a>: <i>Boolean</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#loadfeedback" title="LoadFeedback">LoadFeedback</a>: <i>Boolean</i>
    <a href="#loadimbalancepercentage" title="LoadImbalancePercentage">LoadImbalancePercentage</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>: <i>Boolean</i>
</pre>

## Properties

#### CnameCoalescingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contract

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultErrorPenalty

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSslClientCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSslClientPrivateKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTimeoutPenalty

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailNotificationList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndUserMappingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadFeedback

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadImbalancePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitOnComplete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultHealthMax

Returns the <code>DefaultHealthMax</code> value.

#### DefaultHealthMultiplier

Returns the <code>DefaultHealthMultiplier</code> value.

#### DefaultHealthThreshold

Returns the <code>DefaultHealthThreshold</code> value.

#### DefaultMaxUnreachablePenalty

Returns the <code>DefaultMaxUnreachablePenalty</code> value.

#### DefaultUnreachableThreshold

Returns the <code>DefaultUnreachableThreshold</code> value.

#### Id

Returns the <code>Id</code> value.

#### MapUpdateInterval

Returns the <code>MapUpdateInterval</code> value.

#### MaxProperties

Returns the <code>MaxProperties</code> value.

#### MaxResources

Returns the <code>MaxResources</code> value.

#### MaxTestTimeout

Returns the <code>MaxTestTimeout</code> value.

#### MaxTtl

Returns the <code>MaxTtl</code> value.

#### MinPingableRegionFraction

Returns the <code>MinPingableRegionFraction</code> value.

#### MinTestInterval

Returns the <code>MinTestInterval</code> value.

#### MinTtl

Returns the <code>MinTtl</code> value.

#### PingInterval

Returns the <code>PingInterval</code> value.

#### PingPacketSize

Returns the <code>PingPacketSize</code> value.

#### RoundRobinPrefix

Returns the <code>RoundRobinPrefix</code> value.

#### ServermonitorLivenessCount

Returns the <code>ServermonitorLivenessCount</code> value.

#### ServermonitorLoadCount

Returns the <code>ServermonitorLoadCount</code> value.

#### ServermonitorPool

Returns the <code>ServermonitorPool</code> value.

