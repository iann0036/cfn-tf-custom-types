# Terraform::AWS::ElasticsearchDomain

CloudFormation equivalent of aws_elasticsearch_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElasticsearchDomain",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accesspolicies" title="AccessPolicies">AccessPolicies</a>" : <i>String</i>,
        "<a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>" : <i>[ &lt;a href=&#34;advancedoptions.md&#34;&gt;AdvancedOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#elasticsearchversion" title="ElasticsearchVersion">ElasticsearchVersion</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#kibanaendpoint" title="KibanaEndpoint">KibanaEndpoint</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>" : <i>[ &lt;a href=&#34;clusterconfig.md&#34;&gt;ClusterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#cognitooptions" title="CognitoOptions">CognitoOptions</a>" : <i>[ &lt;a href=&#34;cognitooptions.md&#34;&gt;CognitoOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#domainendpointoptions" title="DomainEndpointOptions">DomainEndpointOptions</a>" : <i>[ &lt;a href=&#34;domainendpointoptions.md&#34;&gt;DomainEndpointOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#ebsoptions" title="EbsOptions">EbsOptions</a>" : <i>[ &lt;a href=&#34;ebsoptions.md&#34;&gt;EbsOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#encryptatrest" title="EncryptAtRest">EncryptAtRest</a>" : <i>[ &lt;a href=&#34;encryptatrest.md&#34;&gt;EncryptAtRest&lt;/a&gt;, ... ]</i>,
        "<a href="#logpublishingoptions" title="LogPublishingOptions">LogPublishingOptions</a>" : <i>[ &lt;a href=&#34;logpublishingoptions.md&#34;&gt;LogPublishingOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#nodetonodeencryption" title="NodeToNodeEncryption">NodeToNodeEncryption</a>" : <i>[ &lt;a href=&#34;nodetonodeencryption.md&#34;&gt;NodeToNodeEncryption&lt;/a&gt;, ... ]</i>,
        "<a href="#snapshotoptions" title="SnapshotOptions">SnapshotOptions</a>" : <i>[ &lt;a href=&#34;snapshotoptions.md&#34;&gt;SnapshotOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#vpcoptions" title="VpcOptions">VpcOptions</a>" : <i>[ &lt;a href=&#34;vpcoptions.md&#34;&gt;VpcOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#zoneawarenessconfig" title="ZoneAwarenessConfig">ZoneAwarenessConfig</a>" : <i>[ &lt;a href=&#34;zoneawarenessconfig.md&#34;&gt;ZoneAwarenessConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElasticsearchDomain
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accesspolicies" title="AccessPolicies">AccessPolicies</a>: <i>String</i>
    <a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>: <i>
      - &lt;a href=&#34;advancedoptions.md&#34;&gt;AdvancedOptions&lt;/a&gt;</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#elasticsearchversion" title="ElasticsearchVersion">ElasticsearchVersion</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#kibanaendpoint" title="KibanaEndpoint">KibanaEndpoint</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#clusterconfig" title="ClusterConfig">ClusterConfig</a>: <i>
      - &lt;a href=&#34;clusterconfig.md&#34;&gt;ClusterConfig&lt;/a&gt;</i>
    <a href="#cognitooptions" title="CognitoOptions">CognitoOptions</a>: <i>
      - &lt;a href=&#34;cognitooptions.md&#34;&gt;CognitoOptions&lt;/a&gt;</i>
    <a href="#domainendpointoptions" title="DomainEndpointOptions">DomainEndpointOptions</a>: <i>
      - &lt;a href=&#34;domainendpointoptions.md&#34;&gt;DomainEndpointOptions&lt;/a&gt;</i>
    <a href="#ebsoptions" title="EbsOptions">EbsOptions</a>: <i>
      - &lt;a href=&#34;ebsoptions.md&#34;&gt;EbsOptions&lt;/a&gt;</i>
    <a href="#encryptatrest" title="EncryptAtRest">EncryptAtRest</a>: <i>
      - &lt;a href=&#34;encryptatrest.md&#34;&gt;EncryptAtRest&lt;/a&gt;</i>
    <a href="#logpublishingoptions" title="LogPublishingOptions">LogPublishingOptions</a>: <i>
      - &lt;a href=&#34;logpublishingoptions.md&#34;&gt;LogPublishingOptions&lt;/a&gt;</i>
    <a href="#nodetonodeencryption" title="NodeToNodeEncryption">NodeToNodeEncryption</a>: <i>
      - &lt;a href=&#34;nodetonodeencryption.md&#34;&gt;NodeToNodeEncryption&lt;/a&gt;</i>
    <a href="#snapshotoptions" title="SnapshotOptions">SnapshotOptions</a>: <i>
      - &lt;a href=&#34;snapshotoptions.md&#34;&gt;SnapshotOptions&lt;/a&gt;</i>
    <a href="#vpcoptions" title="VpcOptions">VpcOptions</a>: <i>
      - &lt;a href=&#34;vpcoptions.md&#34;&gt;VpcOptions&lt;/a&gt;</i>
    <a href="#zoneawarenessconfig" title="ZoneAwarenessConfig">ZoneAwarenessConfig</a>: <i>
      - &lt;a href=&#34;zoneawarenessconfig.md&#34;&gt;ZoneAwarenessConfig&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessPolicies

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedOptions

_Required_: No

_Type_: List of &lt;a href=&#34;advancedoptions.md&#34;&gt;AdvancedOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KibanaEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;clusterconfig.md&#34;&gt;ClusterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CognitoOptions

_Required_: No

_Type_: List of &lt;a href=&#34;cognitooptions.md&#34;&gt;CognitoOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainEndpointOptions

_Required_: No

_Type_: List of &lt;a href=&#34;domainendpointoptions.md&#34;&gt;DomainEndpointOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptions

_Required_: No

_Type_: List of &lt;a href=&#34;ebsoptions.md&#34;&gt;EbsOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptAtRest

_Required_: No

_Type_: List of &lt;a href=&#34;encryptatrest.md&#34;&gt;EncryptAtRest&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPublishingOptions

_Required_: No

_Type_: List of &lt;a href=&#34;logpublishingoptions.md&#34;&gt;LogPublishingOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeToNodeEncryption

_Required_: No

_Type_: List of &lt;a href=&#34;nodetonodeencryption.md&#34;&gt;NodeToNodeEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotOptions

_Required_: No

_Type_: List of &lt;a href=&#34;snapshotoptions.md&#34;&gt;SnapshotOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcOptions

_Required_: No

_Type_: List of &lt;a href=&#34;vpcoptions.md&#34;&gt;VpcOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneAwarenessConfig

_Required_: No

_Type_: List of &lt;a href=&#34;zoneawarenessconfig.md&#34;&gt;ZoneAwarenessConfig&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### DomainId

Returns the &lt;code&gt;DomainId&lt;/code&gt; value.

#### Endpoint

Returns the &lt;code&gt;Endpoint&lt;/code&gt; value.

#### KibanaEndpoint

Returns the &lt;code&gt;KibanaEndpoint&lt;/code&gt; value.

