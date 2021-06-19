# TF::AWS::ElasticsearchDomain

Manages an AWS Elasticsearch Domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ElasticsearchDomain",
    "Properties" : {
        "<a href="#accesspolicies" title="AccessPolicies">AccessPolicies</a>" : <i>String</i>,
        "<a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>" : <i>[ <a href="advancedoptionsdefinition.md">AdvancedOptionsDefinition</a>, ... ]</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#elasticsearchversion" title="ElasticsearchVersion">ElasticsearchVersion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#advancedsecurityoptions" title="AdvancedSecurityOptions">AdvancedSecurityOptions</a>" : <i>[ <a href="advancedsecurityoptionsdefinition.md">AdvancedSecurityOptionsDefinition</a>, ... ]</i>,
        "<a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>" : <i>[ <a href="clusterconfigdefinition.md">ClusterConfigDefinition</a>, ... ]</i>,
        "<a href="#cognitooptions" title="CognitoOptions">CognitoOptions</a>" : <i>[ <a href="cognitooptionsdefinition.md">CognitoOptionsDefinition</a>, ... ]</i>,
        "<a href="#domainendpointoptions" title="DomainEndpointOptions">DomainEndpointOptions</a>" : <i>[ <a href="domainendpointoptionsdefinition.md">DomainEndpointOptionsDefinition</a>, ... ]</i>,
        "<a href="#ebsoptions" title="EbsOptions">EbsOptions</a>" : <i>[ <a href="ebsoptionsdefinition.md">EbsOptionsDefinition</a>, ... ]</i>,
        "<a href="#encryptatrest" title="EncryptAtRest">EncryptAtRest</a>" : <i>[ <a href="encryptatrestdefinition.md">EncryptAtRestDefinition</a>, ... ]</i>,
        "<a href="#logpublishingoptions" title="LogPublishingOptions">LogPublishingOptions</a>" : <i>[ <a href="logpublishingoptionsdefinition.md">LogPublishingOptionsDefinition</a>, ... ]</i>,
        "<a href="#nodetonodeencryption" title="NodeToNodeEncryption">NodeToNodeEncryption</a>" : <i>[ <a href="nodetonodeencryptiondefinition.md">NodeToNodeEncryptionDefinition</a>, ... ]</i>,
        "<a href="#snapshotoptions" title="SnapshotOptions">SnapshotOptions</a>" : <i>[ <a href="snapshotoptionsdefinition.md">SnapshotOptionsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vpcoptions" title="VpcOptions">VpcOptions</a>" : <i>[ <a href="vpcoptionsdefinition.md">VpcOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ElasticsearchDomain
Properties:
    <a href="#accesspolicies" title="AccessPolicies">AccessPolicies</a>: <i>String</i>
    <a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>: <i>
      - <a href="advancedoptionsdefinition.md">AdvancedOptionsDefinition</a></i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#elasticsearchversion" title="ElasticsearchVersion">ElasticsearchVersion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#advancedsecurityoptions" title="AdvancedSecurityOptions">AdvancedSecurityOptions</a>: <i>
      - <a href="advancedsecurityoptionsdefinition.md">AdvancedSecurityOptionsDefinition</a></i>
    <a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>: <i>
      - <a href="clusterconfigdefinition.md">ClusterConfigDefinition</a></i>
    <a href="#cognitooptions" title="CognitoOptions">CognitoOptions</a>: <i>
      - <a href="cognitooptionsdefinition.md">CognitoOptionsDefinition</a></i>
    <a href="#domainendpointoptions" title="DomainEndpointOptions">DomainEndpointOptions</a>: <i>
      - <a href="domainendpointoptionsdefinition.md">DomainEndpointOptionsDefinition</a></i>
    <a href="#ebsoptions" title="EbsOptions">EbsOptions</a>: <i>
      - <a href="ebsoptionsdefinition.md">EbsOptionsDefinition</a></i>
    <a href="#encryptatrest" title="EncryptAtRest">EncryptAtRest</a>: <i>
      - <a href="encryptatrestdefinition.md">EncryptAtRestDefinition</a></i>
    <a href="#logpublishingoptions" title="LogPublishingOptions">LogPublishingOptions</a>: <i>
      - <a href="logpublishingoptionsdefinition.md">LogPublishingOptionsDefinition</a></i>
    <a href="#nodetonodeencryption" title="NodeToNodeEncryption">NodeToNodeEncryption</a>: <i>
      - <a href="nodetonodeencryptiondefinition.md">NodeToNodeEncryptionDefinition</a></i>
    <a href="#snapshotoptions" title="SnapshotOptions">SnapshotOptions</a>: <i>
      - <a href="snapshotoptionsdefinition.md">SnapshotOptionsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vpcoptions" title="VpcOptions">VpcOptions</a>: <i>
      - <a href="vpcoptionsdefinition.md">VpcOptionsDefinition</a></i>
</pre>

## Properties

#### AccessPolicies

IAM policy document specifying the access policies for the domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedOptions

Key-value string pairs to specify advanced configuration options. Note that the values for these configuration options must be strings (wrapped in quotes) or they may be wrong and cause a perpetual diff, causing Terraform to want to recreate your Elasticsearch domain on every apply.

_Required_: No

_Type_: List of <a href="advancedoptionsdefinition.md">AdvancedOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

Name of the domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchVersion

Version of Elasticsearch to deploy. Defaults to `1.5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedSecurityOptions

_Required_: No

_Type_: List of <a href="advancedsecurityoptionsdefinition.md">AdvancedSecurityOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterConfig

_Required_: No

_Type_: List of <a href="clusterconfigdefinition.md">ClusterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CognitoOptions

_Required_: No

_Type_: List of <a href="cognitooptionsdefinition.md">CognitoOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainEndpointOptions

_Required_: No

_Type_: List of <a href="domainendpointoptionsdefinition.md">DomainEndpointOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptions

_Required_: No

_Type_: List of <a href="ebsoptionsdefinition.md">EbsOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptAtRest

_Required_: No

_Type_: List of <a href="encryptatrestdefinition.md">EncryptAtRestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPublishingOptions

_Required_: No

_Type_: List of <a href="logpublishingoptionsdefinition.md">LogPublishingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeToNodeEncryption

_Required_: No

_Type_: List of <a href="nodetonodeencryptiondefinition.md">NodeToNodeEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotOptions

_Required_: No

_Type_: List of <a href="snapshotoptionsdefinition.md">SnapshotOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcOptions

_Required_: No

_Type_: List of <a href="vpcoptionsdefinition.md">VpcOptionsDefinition</a>

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

