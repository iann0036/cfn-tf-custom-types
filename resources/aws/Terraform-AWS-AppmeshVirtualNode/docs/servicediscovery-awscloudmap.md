# Terraform::AWS::AppmeshVirtualNode ServiceDiscovery AwsCloudMap

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attributes" title="Attributes">Attributes</a>" : <i>[ <a href="servicediscovery-awscloudmap-attributes.md">Attributes</a>, ... ]</i>,
    "<a href="#namespacename" title="NamespaceName">NamespaceName</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#attributes" title="Attributes">Attributes</a>: <i>
      - <a href="servicediscovery-awscloudmap-attributes.md">Attributes</a></i>
<a href="#namespacename" title="NamespaceName">NamespaceName</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### Attributes

A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.

_Required_: No

_Type_: List of <a href="servicediscovery-awscloudmap-attributes.md">Attributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceName

The name of the AWS Cloud Map namespace to use.
Use the [`aws_service_discovery_http_namespace`](/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The name of the AWS Cloud Map service to use. Use the [`aws_service_discovery_service`](/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

