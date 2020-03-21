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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#isipv6enabled" title="IsIpv6Enabled">IsIpv6Enabled</a>" : <i>Boolean</i>,
        "<a href="#priceclass" title="PriceClass">PriceClass</a>" : <i>String</i>,
        "<a href="#retainondelete" title="RetainOnDelete">RetainOnDelete</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#waitfordeployment" title="WaitForDeployment">WaitForDeployment</a>" : <i>Boolean</i>,
        "<a href="#webaclid" title="WebAclId">WebAclId</a>" : <i>String</i>,
        "<a href="#cachebehavior" title="CacheBehavior">CacheBehavior</a>" : <i>[ &lt;a href=&#34;cachebehavior.md&#34;&gt;CacheBehavior&lt;/a&gt;, ... ]</i>,
        "<a href="#customerrorresponse" title="CustomErrorResponse">CustomErrorResponse</a>" : <i>[ &lt;a href=&#34;customerrorresponse.md&#34;&gt;CustomErrorResponse&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultcachebehavior" title="DefaultCacheBehavior">DefaultCacheBehavior</a>" : <i>[ &lt;a href=&#34;defaultcachebehavior.md&#34;&gt;DefaultCacheBehavior&lt;/a&gt;, ... ]</i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ &lt;a href=&#34;loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#orderedcachebehavior" title="OrderedCacheBehavior">OrderedCacheBehavior</a>" : <i>[ &lt;a href=&#34;orderedcachebehavior.md&#34;&gt;OrderedCacheBehavior&lt;/a&gt;, ... ]</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>[ &lt;a href=&#34;origin.md&#34;&gt;Origin&lt;/a&gt;, ... ]</i>,
        "<a href="#origingroup" title="OriginGroup">OriginGroup</a>" : <i>[ &lt;a href=&#34;origingroup.md&#34;&gt;OriginGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;, ... ]</i>,
        "<a href="#viewercertificate" title="ViewerCertificate">ViewerCertificate</a>" : <i>[ &lt;a href=&#34;viewercertificate.md&#34;&gt;ViewerCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#forwardedvalues" title="ForwardedValues">ForwardedValues</a>" : <i>[ &lt;a href=&#34;forwardedvalues.md&#34;&gt;ForwardedValues&lt;/a&gt;, ... ]</i>,
        "<a href="#lambdafunctionassociation" title="LambdaFunctionAssociation">LambdaFunctionAssociation</a>" : <i>[ &lt;a href=&#34;lambdafunctionassociation.md&#34;&gt;LambdaFunctionAssociation&lt;/a&gt;, ... ]</i>,
        "<a href="#customheader" title="CustomHeader">CustomHeader</a>" : <i>[ &lt;a href=&#34;customheader.md&#34;&gt;CustomHeader&lt;/a&gt;, ... ]</i>,
        "<a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>" : <i>[ &lt;a href=&#34;customoriginconfig.md&#34;&gt;CustomOriginConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>" : <i>[ &lt;a href=&#34;s3originconfig.md&#34;&gt;S3OriginConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>" : <i>[ &lt;a href=&#34;failovercriteria.md&#34;&gt;FailoverCriteria&lt;/a&gt;, ... ]</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ &lt;a href=&#34;member.md&#34;&gt;Member&lt;/a&gt;, ... ]</i>,
        "<a href="#georestriction" title="GeoRestriction">GeoRestriction</a>" : <i>[ &lt;a href=&#34;georestriction.md&#34;&gt;GeoRestriction&lt;/a&gt;, ... ]</i>,
        "<a href="#cookies" title="Cookies">Cookies</a>" : <i>[ &lt;a href=&#34;cookies.md&#34;&gt;Cookies&lt;/a&gt;, ... ]</i>
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#isipv6enabled" title="IsIpv6Enabled">IsIpv6Enabled</a>: <i>Boolean</i>
    <a href="#priceclass" title="PriceClass">PriceClass</a>: <i>String</i>
    <a href="#retainondelete" title="RetainOnDelete">RetainOnDelete</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#waitfordeployment" title="WaitForDeployment">WaitForDeployment</a>: <i>Boolean</i>
    <a href="#webaclid" title="WebAclId">WebAclId</a>: <i>String</i>
    <a href="#cachebehavior" title="CacheBehavior">CacheBehavior</a>: <i>
      - &lt;a href=&#34;cachebehavior.md&#34;&gt;CacheBehavior&lt;/a&gt;</i>
    <a href="#customerrorresponse" title="CustomErrorResponse">CustomErrorResponse</a>: <i>
      - &lt;a href=&#34;customerrorresponse.md&#34;&gt;CustomErrorResponse&lt;/a&gt;</i>
    <a href="#defaultcachebehavior" title="DefaultCacheBehavior">DefaultCacheBehavior</a>: <i>
      - &lt;a href=&#34;defaultcachebehavior.md&#34;&gt;DefaultCacheBehavior&lt;/a&gt;</i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - &lt;a href=&#34;loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;</i>
    <a href="#orderedcachebehavior" title="OrderedCacheBehavior">OrderedCacheBehavior</a>: <i>
      - &lt;a href=&#34;orderedcachebehavior.md&#34;&gt;OrderedCacheBehavior&lt;/a&gt;</i>
    <a href="#origin" title="Origin">Origin</a>: <i>
      - &lt;a href=&#34;origin.md&#34;&gt;Origin&lt;/a&gt;</i>
    <a href="#origingroup" title="OriginGroup">OriginGroup</a>: <i>
      - &lt;a href=&#34;origingroup.md&#34;&gt;OriginGroup&lt;/a&gt;</i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;</i>
    <a href="#viewercertificate" title="ViewerCertificate">ViewerCertificate</a>: <i>
      - &lt;a href=&#34;viewercertificate.md&#34;&gt;ViewerCertificate&lt;/a&gt;</i>
    <a href="#forwardedvalues" title="ForwardedValues">ForwardedValues</a>: <i>
      - &lt;a href=&#34;forwardedvalues.md&#34;&gt;ForwardedValues&lt;/a&gt;</i>
    <a href="#lambdafunctionassociation" title="LambdaFunctionAssociation">LambdaFunctionAssociation</a>: <i>
      - &lt;a href=&#34;lambdafunctionassociation.md&#34;&gt;LambdaFunctionAssociation&lt;/a&gt;</i>
    <a href="#customheader" title="CustomHeader">CustomHeader</a>: <i>
      - &lt;a href=&#34;customheader.md&#34;&gt;CustomHeader&lt;/a&gt;</i>
    <a href="#customoriginconfig" title="CustomOriginConfig">CustomOriginConfig</a>: <i>
      - &lt;a href=&#34;customoriginconfig.md&#34;&gt;CustomOriginConfig&lt;/a&gt;</i>
    <a href="#s3originconfig" title="S3OriginConfig">S3OriginConfig</a>: <i>
      - &lt;a href=&#34;s3originconfig.md&#34;&gt;S3OriginConfig&lt;/a&gt;</i>
    <a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>: <i>
      - &lt;a href=&#34;failovercriteria.md&#34;&gt;FailoverCriteria&lt;/a&gt;</i>
    <a href="#member" title="Member">Member</a>: <i>
      - &lt;a href=&#34;member.md&#34;&gt;Member&lt;/a&gt;</i>
    <a href="#georestriction" title="GeoRestriction">GeoRestriction</a>: <i>
      - &lt;a href=&#34;georestriction.md&#34;&gt;GeoRestriction&lt;/a&gt;</i>
    <a href="#cookies" title="Cookies">Cookies</a>: <i>
      - &lt;a href=&#34;cookies.md&#34;&gt;Cookies&lt;/a&gt;</i>
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

#### Id

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

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;cachebehavior.md&#34;&gt;CacheBehavior&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrorResponse

_Required_: No

_Type_: List of &lt;a href=&#34;customerrorresponse.md&#34;&gt;CustomErrorResponse&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCacheBehavior

_Required_: No

_Type_: List of &lt;a href=&#34;defaultcachebehavior.md&#34;&gt;DefaultCacheBehavior&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of &lt;a href=&#34;loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedCacheBehavior

_Required_: No

_Type_: List of &lt;a href=&#34;orderedcachebehavior.md&#34;&gt;OrderedCacheBehavior&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of &lt;a href=&#34;origin.md&#34;&gt;Origin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroup

_Required_: No

_Type_: List of &lt;a href=&#34;origingroup.md&#34;&gt;OriginGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewerCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;viewercertificate.md&#34;&gt;ViewerCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardedValues

_Required_: No

_Type_: List of &lt;a href=&#34;forwardedvalues.md&#34;&gt;ForwardedValues&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunctionAssociation

_Required_: No

_Type_: List of &lt;a href=&#34;lambdafunctionassociation.md&#34;&gt;LambdaFunctionAssociation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeader

_Required_: No

_Type_: List of &lt;a href=&#34;customheader.md&#34;&gt;CustomHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomOriginConfig

_Required_: No

_Type_: List of &lt;a href=&#34;customoriginconfig.md&#34;&gt;CustomOriginConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3OriginConfig

_Required_: No

_Type_: List of &lt;a href=&#34;s3originconfig.md&#34;&gt;S3OriginConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverCriteria

_Required_: No

_Type_: List of &lt;a href=&#34;failovercriteria.md&#34;&gt;FailoverCriteria&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of &lt;a href=&#34;member.md&#34;&gt;Member&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoRestriction

_Required_: No

_Type_: List of &lt;a href=&#34;georestriction.md&#34;&gt;GeoRestriction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookies

_Required_: No

_Type_: List of &lt;a href=&#34;cookies.md&#34;&gt;Cookies&lt;/a&gt;

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

Returns the &lt;code&gt;ActiveTrustedSigners&lt;/code&gt; value.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CallerReference

Returns the &lt;code&gt;CallerReference&lt;/code&gt; value.

#### DomainName

Returns the &lt;code&gt;DomainName&lt;/code&gt; value.

#### Etag

Returns the &lt;code&gt;Etag&lt;/code&gt; value.

#### HostedZoneId

Returns the &lt;code&gt;HostedZoneId&lt;/code&gt; value.

#### InProgressValidationBatches

Returns the &lt;code&gt;InProgressValidationBatches&lt;/code&gt; value.

#### LastModifiedTime

Returns the &lt;code&gt;LastModifiedTime&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

