# TF::AWS::AppmeshVirtualNode ServiceDiscoveryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awscloudmap" title="AwsCloudMap">AwsCloudMap</a>" : <i>[ <a href="awscloudmapdefinition.md">AwsCloudMapDefinition</a>, ... ]</i>,
    "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dnsdefinition.md">DnsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awscloudmap" title="AwsCloudMap">AwsCloudMap</a>: <i>
      - <a href="awscloudmapdefinition.md">AwsCloudMapDefinition</a></i>
<a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dnsdefinition.md">DnsDefinition</a></i>
</pre>

## Properties

#### AwsCloudMap

_Required_: No

_Type_: List of <a href="awscloudmapdefinition.md">AwsCloudMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of <a href="dnsdefinition.md">DnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

