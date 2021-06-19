# TF::AWS::CloudfrontDistribution

Creates an Amazon CloudFront web distribution.

For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For specific information about creating
CloudFront web distributions, see the [POST Distribution][2] page in the Amazon
CloudFront API Reference.

~> **NOTE:** CloudFront distributions take about 15 minutes to a deployed state
after creation or modification. During this time, deletes to resources will be
blocked. If you need to delete a distribution that is enabled and you do not
want to wait, you need to use the `retain_on_delete` flag.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudfrontDistribution",
    "Properties" : {
        "<a href="#aliases" title="Aliases">Aliases</a>" : <i>[ String, ... ]</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#defaultrootobject" title="DefaultRootObject">DefaultRootObject</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpversion" title="HttpVersion">HttpVersion</a>" : <i>String</i>,
        "<a href="#isipv6enabled" title="IsIpv6Enabled">IsIpv6Enabled</a>" : <i>Boolean</i>,
        "<a href="#priceclass" title="PriceClass">PriceClass</a>" : <i>String</i>,
        "<a href="#retainondelete" title="RetainOnDelete">RetainOnDelete</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#waitfordeployment" title="WaitForDeployment">WaitForDeployment</a>" : <i>Boolean</i>,
        "<a href="#webaclid" title="WebAclId">WebAclId</a>" : <i>String</i>,
        "<a href="#customerrorresponse" title="CustomErrorResponse">CustomErrorResponse</a>" : <i>[ <a href="customerrorresponsedefinition.md">CustomErrorResponseDefinition</a>, ... ]</i>,
        "<a href="#defaultcachebehavior" title="DefaultCacheBehavior">DefaultCacheBehavior</a>" : <i>[ <a href="defaultcachebehaviordefinition.md">DefaultCacheBehaviorDefinition</a>, ... ]</i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a>, ... ]</i>,
        "<a href="#orderedcachebehavior" title="OrderedCacheBehavior">OrderedCacheBehavior</a>" : <i>[ <a href="orderedcachebehaviordefinition.md">OrderedCacheBehaviorDefinition</a>, ... ]</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origindefinition.md">OriginDefinition</a>, ... ]</i>,
        "<a href="#origingroup" title="OriginGroup">OriginGroup</a>" : <i>[ <a href="origingroupdefinition.md">OriginGroupDefinition</a>, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ <a href="restrictionsdefinition.md">RestrictionsDefinition</a>, ... ]</i>,
        "<a href="#viewercertificate" title="ViewerCertificate">ViewerCertificate</a>" : <i>[ <a href="viewercertificatedefinition.md">ViewerCertificateDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudfrontDistribution
Properties:
    <a href="#aliases" title="Aliases">Aliases</a>: <i>
      - String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#defaultrootobject" title="DefaultRootObject">DefaultRootObject</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#httpversion" title="HttpVersion">HttpVersion</a>: <i>String</i>
    <a href="#isipv6enabled" title="IsIpv6Enabled">IsIpv6Enabled</a>: <i>Boolean</i>
    <a href="#priceclass" title="PriceClass">PriceClass</a>: <i>String</i>
    <a href="#retainondelete" title="RetainOnDelete">RetainOnDelete</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#waitfordeployment" title="WaitForDeployment">WaitForDeployment</a>: <i>Boolean</i>
    <a href="#webaclid" title="WebAclId">WebAclId</a>: <i>String</i>
    <a href="#customerrorresponse" title="CustomErrorResponse">CustomErrorResponse</a>: <i>
      - <a href="customerrorresponsedefinition.md">CustomErrorResponseDefinition</a></i>
    <a href="#defaultcachebehavior" title="DefaultCacheBehavior">DefaultCacheBehavior</a>: <i>
      - <a href="defaultcachebehaviordefinition.md">DefaultCacheBehaviorDefinition</a></i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a></i>
    <a href="#orderedcachebehavior" title="OrderedCacheBehavior">OrderedCacheBehavior</a>: <i>
      - <a href="orderedcachebehaviordefinition.md">OrderedCacheBehaviorDefinition</a></i>
    <a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origindefinition.md">OriginDefinition</a></i>
    <a href="#origingroup" title="OriginGroup">OriginGroup</a>: <i>
      - <a href="origingroupdefinition.md">OriginGroupDefinition</a></i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - <a href="restrictionsdefinition.md">RestrictionsDefinition</a></i>
    <a href="#viewercertificate" title="ViewerCertificate">ViewerCertificate</a>: <i>
      - <a href="viewercertificatedefinition.md">ViewerCertificateDefinition</a></i>
</pre>

## Properties

#### Aliases

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRootObject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsIpv6Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriceClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainOnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForDeployment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAclId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorResponse

_Required_: No

_Type_: List of <a href="customerrorresponsedefinition.md">CustomErrorResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCacheBehavior

_Required_: No

_Type_: List of <a href="defaultcachebehaviordefinition.md">DefaultCacheBehaviorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedCacheBehavior

_Required_: No

_Type_: List of <a href="orderedcachebehaviordefinition.md">OrderedCacheBehaviorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origindefinition.md">OriginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroup

_Required_: No

_Type_: List of <a href="origingroupdefinition.md">OriginGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of <a href="restrictionsdefinition.md">RestrictionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewerCertificate

_Required_: No

_Type_: List of <a href="viewercertificatedefinition.md">ViewerCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CallerReference

Returns the <code>CallerReference</code> value.

#### DomainName

Returns the <code>DomainName</code> value.

#### Etag

Returns the <code>Etag</code> value.

#### HostedZoneId

Returns the <code>HostedZoneId</code> value.

#### Id

Returns the <code>Id</code> value.

#### InProgressValidationBatches

Returns the <code>InProgressValidationBatches</code> value.

#### LastModifiedTime

Returns the <code>LastModifiedTime</code> value.

#### Status

Returns the <code>Status</code> value.

#### TrustedKeyGroups

Returns the <code>TrustedKeyGroups</code> value.

#### TrustedSigners

Returns the <code>TrustedSigners</code> value.

