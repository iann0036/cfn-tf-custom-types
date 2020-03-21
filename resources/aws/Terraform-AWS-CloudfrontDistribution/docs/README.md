# Terraform::AWS::CloudfrontDistribution

CloudFormation equivalent of aws_cloudfront_distribution

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CloudfrontDistribution",
    "Properties" : {
        "<a href="#aliases" title="Aliases">Aliases</a>" : <i>[ String, ... ]</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#defaultrootobject" title="DefaultRootObject">DefaultRootObject</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#httpversion" title="HttpVersion">HttpVersion</a>" : <i>String</i>,
        "<a href="#isipv6enabled" title="IsIpv6Enabled">IsIpv6Enabled</a>" : <i>Boolean</i>,
        "<a href="#priceclass" title="PriceClass">PriceClass</a>" : <i>String</i>,
        "<a href="#retainondelete" title="RetainOnDelete">RetainOnDelete</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#waitfordeployment" title="WaitForDeployment">WaitForDeployment</a>" : <i>Boolean</i>,
        "<a href="#webaclid" title="WebAclId">WebAclId</a>" : <i>String</i>,
        "<a href="#cachebehavior" title="CacheBehavior">CacheBehavior</a>" : <i>[ <a href="cachebehavior.md">CacheBehavior</a>, ... ]</i>,
        "<a href="#customerrorresponse" title="CustomErrorResponse">CustomErrorResponse</a>" : <i>[ <a href="customerrorresponse.md">CustomErrorResponse</a>, ... ]</i>,
        "<a href="#defaultcachebehavior" title="DefaultCacheBehavior">DefaultCacheBehavior</a>" : <i>[ <a href="defaultcachebehavior.md">DefaultCacheBehavior</a>, ... ]</i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ <a href="loggingconfig.md">LoggingConfig</a>, ... ]</i>,
        "<a href="#orderedcachebehavior" title="OrderedCacheBehavior">OrderedCacheBehavior</a>" : <i>[ <a href="orderedcachebehavior.md">OrderedCacheBehavior</a>, ... ]</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origin.md">Origin</a>, ... ]</i>,
        "<a href="#origingroup" title="OriginGroup">OriginGroup</a>" : <i>[ <a href="origingroup.md">OriginGroup</a>, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ <a href="restrictions.md">Restrictions</a>, ... ]</i>,
        "<a href="#viewercertificate" title="ViewerCertificate">ViewerCertificate</a>" : <i>[ <a href="viewercertificate.md">ViewerCertificate</a>, ... ]</i>,
        "<a href="#forwardedvalues" title="ForwardedValues">ForwardedValues</a>" : <i>[ <a href="forwardedvalues.md">ForwardedValues</a>, ... ]</i>,
        "<a href="#lambdafunctionassociation" title="LambdaFunctionAssociation">LambdaFunctionAssociation</a>" : <i>[ <a href="lambdafunctionassociation.md">LambdaFunctionAssociation</a>, ... ]</i>,
        "<a href="#customheader" title="CustomHeader">CustomHeader</a>" : <i>[ <a href="customheader.md">CustomHeader</a>, ... ]</i>,
        "<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>" : <i>[ <a href="customoriginconfig.md">CustomOriginConfig</a>, ... ]</i>,
        "<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>" : <i>[ <a href="s3originconfig.md">S3OriginConfig</a>, ... ]</i>,
        "<a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>" : <i>[ <a href="failovercriteria.md">FailoverCriteria</a>, ... ]</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="member.md">Member</a>, ... ]</i>,
        "<a href="#georestriction" title="GeoRestriction">GeoRestriction</a>" : <i>[ <a href="georestriction.md">GeoRestriction</a>, ... ]</i>,
        "<a href="#cookies" title="Cookies">Cookies</a>" : <i>[ <a href="cookies.md">Cookies</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CloudfrontDistribution
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
      - <a href="tags.md">Tags</a></i>
    <a href="#waitfordeployment" title="WaitForDeployment">WaitForDeployment</a>: <i>Boolean</i>
    <a href="#webaclid" title="WebAclId">WebAclId</a>: <i>String</i>
    <a href="#cachebehavior" title="CacheBehavior">CacheBehavior</a>: <i>
      - <a href="cachebehavior.md">CacheBehavior</a></i>
    <a href="#customerrorresponse" title="CustomErrorResponse">CustomErrorResponse</a>: <i>
      - <a href="customerrorresponse.md">CustomErrorResponse</a></i>
    <a href="#defaultcachebehavior" title="DefaultCacheBehavior">DefaultCacheBehavior</a>: <i>
      - <a href="defaultcachebehavior.md">DefaultCacheBehavior</a></i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - <a href="loggingconfig.md">LoggingConfig</a></i>
    <a href="#orderedcachebehavior" title="OrderedCacheBehavior">OrderedCacheBehavior</a>: <i>
      - <a href="orderedcachebehavior.md">OrderedCacheBehavior</a></i>
    <a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origin.md">Origin</a></i>
    <a href="#origingroup" title="OriginGroup">OriginGroup</a>: <i>
      - <a href="origingroup.md">OriginGroup</a></i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - <a href="restrictions.md">Restrictions</a></i>
    <a href="#viewercertificate" title="ViewerCertificate">ViewerCertificate</a>: <i>
      - <a href="viewercertificate.md">ViewerCertificate</a></i>
    <a href="#forwardedvalues" title="ForwardedValues">ForwardedValues</a>: <i>
      - <a href="forwardedvalues.md">ForwardedValues</a></i>
    <a href="#lambdafunctionassociation" title="LambdaFunctionAssociation">LambdaFunctionAssociation</a>: <i>
      - <a href="lambdafunctionassociation.md">LambdaFunctionAssociation</a></i>
    <a href="#customheader" title="CustomHeader">CustomHeader</a>: <i>
      - <a href="customheader.md">CustomHeader</a></i>
    <a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>: <i>
      - <a href="customoriginconfig.md">CustomOriginConfig</a></i>
    <a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>: <i>
      - <a href="s3originconfig.md">S3OriginConfig</a></i>
    <a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>: <i>
      - <a href="failovercriteria.md">FailoverCriteria</a></i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="member.md">Member</a></i>
    <a href="#georestriction" title="GeoRestriction">GeoRestriction</a>: <i>
      - <a href="georestriction.md">GeoRestriction</a></i>
    <a href="#cookies" title="Cookies">Cookies</a>: <i>
      - <a href="cookies.md">Cookies</a></i>
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

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForDeployment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAclId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheBehavior

_Required_: No

_Type_: List of <a href="cachebehavior.md">CacheBehavior</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorResponse

_Required_: No

_Type_: List of <a href="customerrorresponse.md">CustomErrorResponse</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCacheBehavior

_Required_: No

_Type_: List of <a href="defaultcachebehavior.md">DefaultCacheBehavior</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of <a href="loggingconfig.md">LoggingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedCacheBehavior

_Required_: No

_Type_: List of <a href="orderedcachebehavior.md">OrderedCacheBehavior</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origin.md">Origin</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroup

_Required_: No

_Type_: List of <a href="origingroup.md">OriginGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of <a href="restrictions.md">Restrictions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewerCertificate

_Required_: No

_Type_: List of <a href="viewercertificate.md">ViewerCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardedValues

_Required_: No

_Type_: List of <a href="forwardedvalues.md">ForwardedValues</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunctionAssociation

_Required_: No

_Type_: List of <a href="lambdafunctionassociation.md">LambdaFunctionAssociation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeader

_Required_: No

_Type_: List of <a href="customheader.md">CustomHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomOriginConfig

_Required_: No

_Type_: List of <a href="customoriginconfig.md">CustomOriginConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3OriginConfig

_Required_: No

_Type_: List of <a href="s3originconfig.md">S3OriginConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverCriteria

_Required_: No

_Type_: List of <a href="failovercriteria.md">FailoverCriteria</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="member.md">Member</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoRestriction

_Required_: No

_Type_: List of <a href="georestriction.md">GeoRestriction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookies

_Required_: No

_Type_: List of <a href="cookies.md">Cookies</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActiveTrustedSigners

Returns the <code>ActiveTrustedSigners</code> value.

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

#### InProgressValidationBatches

Returns the <code>InProgressValidationBatches</code> value.

#### LastModifiedTime

Returns the <code>LastModifiedTime</code> value.

#### Status

Returns the <code>Status</code> value.

