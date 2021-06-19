# TF::Akamai::DnsRecord

Use the `akamai_dns_record` resource to configure a DNS record that can integrate with your existing DNS infrastructure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::DnsRecord",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>Double</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#digest" title="Digest">Digest</a>" : <i>String</i>,
        "<a href="#digesttype" title="DigestType">DigestType</a>" : <i>Double</i>,
        "<a href="#emailaddress" title="EmailAddress">EmailAddress</a>" : <i>String</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>String</i>,
        "<a href="#expiry" title="Expiry">Expiry</a>" : <i>Double</i>,
        "<a href="#fingerprint" title="Fingerprint">Fingerprint</a>" : <i>String</i>,
        "<a href="#fingerprinttype" title="FingerprintType">FingerprintType</a>" : <i>Double</i>,
        "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
        "<a href="#flagsnaptr" title="Flagsnaptr">Flagsnaptr</a>" : <i>String</i>,
        "<a href="#hardware" title="Hardware">Hardware</a>" : <i>String</i>,
        "<a href="#inception" title="Inception">Inception</a>" : <i>String</i>,
        "<a href="#iterations" title="Iterations">Iterations</a>" : <i>Double</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keytag" title="Keytag">Keytag</a>" : <i>Double</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>Double</i>,
        "<a href="#mailbox" title="Mailbox">Mailbox</a>" : <i>String</i>,
        "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameserver" title="NameServer">NameServer</a>" : <i>String</i>,
        "<a href="#nexthashedownername" title="NextHashedOwnerName">NextHashedOwnerName</a>" : <i>String</i>,
        "<a href="#nxdomainttl" title="NxdomainTtl">NxdomainTtl</a>" : <i>Double</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#originalttl" title="OriginalTtl">OriginalTtl</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#preference" title="Preference">Preference</a>" : <i>Double</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#priorityincrement" title="PriorityIncrement">PriorityIncrement</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
        "<a href="#recordtype" title="Recordtype">Recordtype</a>" : <i>String</i>,
        "<a href="#refresh" title="Refresh">Refresh</a>" : <i>Double</i>,
        "<a href="#regexp" title="Regexp">Regexp</a>" : <i>String</i>,
        "<a href="#replacement" title="Replacement">Replacement</a>" : <i>String</i>,
        "<a href="#retry" title="Retry">Retry</a>" : <i>Double</i>,
        "<a href="#salt" title="Salt">Salt</a>" : <i>String</i>,
        "<a href="#selector" title="Selector">Selector</a>" : <i>Double</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#signature" title="Signature">Signature</a>" : <i>String</i>,
        "<a href="#signer" title="Signer">Signer</a>" : <i>String</i>,
        "<a href="#software" title="Software">Software</a>" : <i>String</i>,
        "<a href="#subtype" title="Subtype">Subtype</a>" : <i>Double</i>,
        "<a href="#svcparams" title="SvcParams">SvcParams</a>" : <i>String</i>,
        "<a href="#svcpriority" title="SvcPriority">SvcPriority</a>" : <i>Double</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetname" title="TargetName">TargetName</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#txt" title="Txt">Txt</a>" : <i>String</i>,
        "<a href="#typebitmaps" title="TypeBitmaps">TypeBitmaps</a>" : <i>String</i>,
        "<a href="#typecovered" title="TypeCovered">TypeCovered</a>" : <i>String</i>,
        "<a href="#typemnemonic" title="TypeMnemonic">TypeMnemonic</a>" : <i>String</i>,
        "<a href="#typevalue" title="TypeValue">TypeValue</a>" : <i>Double</i>,
        "<a href="#usage" title="Usage">Usage</a>" : <i>Double</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::DnsRecord
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>Double</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#digest" title="Digest">Digest</a>: <i>String</i>
    <a href="#digesttype" title="DigestType">DigestType</a>: <i>Double</i>
    <a href="#emailaddress" title="EmailAddress">EmailAddress</a>: <i>String</i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>String</i>
    <a href="#expiry" title="Expiry">Expiry</a>: <i>Double</i>
    <a href="#fingerprint" title="Fingerprint">Fingerprint</a>: <i>String</i>
    <a href="#fingerprinttype" title="FingerprintType">FingerprintType</a>: <i>Double</i>
    <a href="#flags" title="Flags">Flags</a>: <i>Double</i>
    <a href="#flagsnaptr" title="Flagsnaptr">Flagsnaptr</a>: <i>String</i>
    <a href="#hardware" title="Hardware">Hardware</a>: <i>String</i>
    <a href="#inception" title="Inception">Inception</a>: <i>String</i>
    <a href="#iterations" title="Iterations">Iterations</a>: <i>Double</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keytag" title="Keytag">Keytag</a>: <i>Double</i>
    <a href="#labels" title="Labels">Labels</a>: <i>Double</i>
    <a href="#mailbox" title="Mailbox">Mailbox</a>: <i>String</i>
    <a href="#matchtype" title="MatchType">MatchType</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameserver" title="NameServer">NameServer</a>: <i>String</i>
    <a href="#nexthashedownername" title="NextHashedOwnerName">NextHashedOwnerName</a>: <i>String</i>
    <a href="#nxdomainttl" title="NxdomainTtl">NxdomainTtl</a>: <i>Double</i>
    <a href="#order" title="Order">Order</a>: <i>Double</i>
    <a href="#originalttl" title="OriginalTtl">OriginalTtl</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#preference" title="Preference">Preference</a>: <i>Double</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#priorityincrement" title="PriorityIncrement">PriorityIncrement</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
    <a href="#recordtype" title="Recordtype">Recordtype</a>: <i>String</i>
    <a href="#refresh" title="Refresh">Refresh</a>: <i>Double</i>
    <a href="#regexp" title="Regexp">Regexp</a>: <i>String</i>
    <a href="#replacement" title="Replacement">Replacement</a>: <i>String</i>
    <a href="#retry" title="Retry">Retry</a>: <i>Double</i>
    <a href="#salt" title="Salt">Salt</a>: <i>String</i>
    <a href="#selector" title="Selector">Selector</a>: <i>Double</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#signature" title="Signature">Signature</a>: <i>String</i>
    <a href="#signer" title="Signer">Signer</a>: <i>String</i>
    <a href="#software" title="Software">Software</a>: <i>String</i>
    <a href="#subtype" title="Subtype">Subtype</a>: <i>Double</i>
    <a href="#svcparams" title="SvcParams">SvcParams</a>: <i>String</i>
    <a href="#svcpriority" title="SvcPriority">SvcPriority</a>: <i>Double</i>
    <a href="#target" title="Target">Target</a>: <i>
      - String</i>
    <a href="#targetname" title="TargetName">TargetName</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#txt" title="Txt">Txt</a>: <i>String</i>
    <a href="#typebitmaps" title="TypeBitmaps">TypeBitmaps</a>: <i>String</i>
    <a href="#typecovered" title="TypeCovered">TypeCovered</a>: <i>String</i>
    <a href="#typemnemonic" title="TypeMnemonic">TypeMnemonic</a>: <i>String</i>
    <a href="#typevalue" title="TypeValue">TypeValue</a>: <i>Double</i>
    <a href="#usage" title="Usage">Usage</a>: <i>Double</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### Active

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algorithm

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Digest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DigestType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FingerprintType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flags

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flagsnaptr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hardware

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inception

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iterations

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keytag

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mailbox

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHashedOwnerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NxdomainTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityIncrement

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recordtype

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Refresh

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regexp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replacement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Salt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signature

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Software

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subtype

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvcParams

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvcPriority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Txt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeBitmaps

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeCovered

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeMnemonic

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AnswerType

Returns the <code>AnswerType</code> value.

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

#### RecordSha

Returns the <code>RecordSha</code> value.

#### Serial

Returns the <code>Serial</code> value.

