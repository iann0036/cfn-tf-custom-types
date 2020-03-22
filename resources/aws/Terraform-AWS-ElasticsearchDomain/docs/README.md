# Terraform::AWS::ElasticsearchDomain

CloudFormation equivalent of aws_elasticsearch_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElasticsearchDomain",
    "Properties" : {
        "<a href="#accesspolicies" title="AccessPolicies">AccessPolicies</a>" : <i>String</i>,
        "<a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>" : <i>[ <a href="advancedoptions.md">AdvancedOptions</a>, ... ]</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#elasticsearchversion" title="ElasticsearchVersion">ElasticsearchVersion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>" : <i>[ <a href="clusterconfig.md">ClusterConfig</a>, ... ]</i>,
        "<a href="#cognitooptions" title="CognitoOptions">CognitoOptions</a>" : <i>[ <a href="cognitooptions.md">CognitoOptions</a>, ... ]</i>,
        "<a href="#domainendpointoptions" title="DomainEndpointOptions">DomainEndpointOptions</a>" : <i>[ <a href="domainendpointoptions.md">DomainEndpointOptions</a>, ... ]</i>,
        "<a href="#ebsoptions" title="EbsOptions">EbsOptions</a>" : <i>[ <a href="ebsoptions.md">EbsOptions</a>, ... ]</i>,
        "<a href="#encryptatrest" title="EncryptAtRest">EncryptAtRest</a>" : <i>[ <a href="encryptatrest.md">EncryptAtRest</a>, ... ]</i>,
        "<a href="#logpublishingoptions" title="LogPublishingOptions">LogPublishingOptions</a>" : <i>[ <a href="logpublishingoptions.md">LogPublishingOptions</a>, ... ]</i>,
        "<a href="#nodetonodeencryption" title="NodeToNodeEncryption">NodeToNodeEncryption</a>" : <i>[ <a href="nodetonodeencryption.md">NodeToNodeEncryption</a>, ... ]</i>,
        "<a href="#snapshotoptions" title="SnapshotOptions">SnapshotOptions</a>" : <i>[ <a href="snapshotoptions.md">SnapshotOptions</a>, ... ]</i>,
        "<a href="#vpcoptions" title="VpcOptions">VpcOptions</a>" : <i>[ <a href="vpcoptions.md">VpcOptions</a>, ... ]</i>,
        "<a href="#zoneawarenessconfig" title="ZoneAwarenessConfig">ZoneAwarenessConfig</a>" : <i>[ <a href="zoneawarenessconfig.md">ZoneAwarenessConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElasticsearchDomain
Properties:
    <a href="#accesspolicies" title="AccessPolicies">AccessPolicies</a>: <i>String</i>
    <a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>: <i>
      - <a href="advancedoptions.md">AdvancedOptions</a></i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#elasticsearchversion" title="ElasticsearchVersion">ElasticsearchVersion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>: <i>
      - <a href="clusterconfig.md">ClusterConfig</a></i>
    <a href="#cognitooptions" title="CognitoOptions">CognitoOptions</a>: <i>
      - <a href="cognitooptions.md">CognitoOptions</a></i>
    <a href="#domainendpointoptions" title="DomainEndpointOptions">DomainEndpointOptions</a>: <i>
      - <a href="domainendpointoptions.md">DomainEndpointOptions</a></i>
    <a href="#ebsoptions" title="EbsOptions">EbsOptions</a>: <i>
      - <a href="ebsoptions.md">EbsOptions</a></i>
    <a href="#encryptatrest" title="EncryptAtRest">EncryptAtRest</a>: <i>
      - <a href="encryptatrest.md">EncryptAtRest</a></i>
    <a href="#logpublishingoptions" title="LogPublishingOptions">LogPublishingOptions</a>: <i>
      - <a href="logpublishingoptions.md">LogPublishingOptions</a></i>
    <a href="#nodetonodeencryption" title="NodeToNodeEncryption">NodeToNodeEncryption</a>: <i>
      - <a href="nodetonodeencryption.md">NodeToNodeEncryption</a></i>
    <a href="#snapshotoptions" title="SnapshotOptions">SnapshotOptions</a>: <i>
      - <a href="snapshotoptions.md">SnapshotOptions</a></i>
    <a href="#vpcoptions" title="VpcOptions">VpcOptions</a>: <i>
      - <a href="vpcoptions.md">VpcOptions</a></i>
    <a href="#zoneawarenessconfig" title="ZoneAwarenessConfig">ZoneAwarenessConfig</a>: <i>
      - <a href="zoneawarenessconfig.md">ZoneAwarenessConfig</a></i>
</pre>

## Properties

#### AccessPolicies

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedOptions

_Required_: No

_Type_: List of <a href="advancedoptions.md">AdvancedOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterConfig

_Required_: No

_Type_: List of <a href="clusterconfig.md">ClusterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CognitoOptions

_Required_: No

_Type_: List of <a href="cognitooptions.md">CognitoOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainEndpointOptions

_Required_: No

_Type_: List of <a href="domainendpointoptions.md">DomainEndpointOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptions

_Required_: No

_Type_: List of <a href="ebsoptions.md">EbsOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptAtRest

_Required_: No

_Type_: List of <a href="encryptatrest.md">EncryptAtRest</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPublishingOptions

_Required_: No

_Type_: List of <a href="logpublishingoptions.md">LogPublishingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeToNodeEncryption

_Required_: No

_Type_: List of <a href="nodetonodeencryption.md">NodeToNodeEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotOptions

_Required_: No

_Type_: List of <a href="snapshotoptions.md">SnapshotOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcOptions

_Required_: No

_Type_: List of <a href="vpcoptions.md">VpcOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneAwarenessConfig

_Required_: No

_Type_: List of <a href="zoneawarenessconfig.md">ZoneAwarenessConfig</a>

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

#### DomainId

Returns the <code>DomainId</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### KibanaEndpoint

Returns the <code>KibanaEndpoint</code> value.

