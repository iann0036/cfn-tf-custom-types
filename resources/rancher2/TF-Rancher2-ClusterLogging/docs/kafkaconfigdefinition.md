# TF::Rancher2::ClusterLogging KafkaConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#brokerendpoints" title="BrokerEndpoints">BrokerEndpoints</a>" : <i>[ String, ... ]</i>,
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#clientcert" title="ClientCert">ClientCert</a>" : <i>String</i>,
    "<a href="#clientkey" title="ClientKey">ClientKey</a>" : <i>String</i>,
    "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>,
    "<a href="#zookeeperendpoint" title="ZookeeperEndpoint">ZookeeperEndpoint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#brokerendpoints" title="BrokerEndpoints">BrokerEndpoints</a>: <i>
      - String</i>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#clientcert" title="ClientCert">ClientCert</a>: <i>String</i>
<a href="#clientkey" title="ClientKey">ClientKey</a>: <i>String</i>
<a href="#topic" title="Topic">Topic</a>: <i>String</i>
<a href="#zookeeperendpoint" title="ZookeeperEndpoint">ZookeeperEndpoint</a>: <i>String</i>
</pre>

## Properties

#### BrokerEndpoints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZookeeperEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

