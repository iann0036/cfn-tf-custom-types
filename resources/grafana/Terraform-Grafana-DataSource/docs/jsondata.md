# Terraform::Grafana::DataSource JsonData

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assumerolearn" title="AssumeRoleArn">AssumeRoleArn</a>" : <i>String</i>,
    "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
    "<a href="#custommetricsnamespaces" title="CustomMetricsNamespaces">CustomMetricsNamespaces</a>" : <i>String</i>,
    "<a href="#defaultregion" title="DefaultRegion">DefaultRegion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#assumerolearn" title="AssumeRoleArn">AssumeRoleArn</a>: <i>String</i>
<a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
<a href="#custommetricsnamespaces" title="CustomMetricsNamespaces">CustomMetricsNamespaces</a>: <i>String</i>
<a href="#defaultregion" title="DefaultRegion">DefaultRegion</a>: <i>String</i>
</pre>

## Properties

#### AssumeRoleArn

The role
ARN to be assumed by Grafana when using the CloudWatch data source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

The authentication type
type used to access the data source.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomMetricsNamespaces

A comma-separated list of custom namespaces to be queried by the CloudWatch
data source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRegion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

