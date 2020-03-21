# Terraform::AWS::AppmeshVirtualNode

CloudFormation equivalent of aws_appmesh_virtual_node

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppmeshVirtualNode",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#meshname" title="MeshName">MeshName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
        "<a href="#listener" title="Listener">Listener</a>" : <i>[ &lt;a href=&#34;listener.md&#34;&gt;Listener&lt;/a&gt;, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
        "<a href="#servicediscovery" title="ServiceDiscovery">ServiceDiscovery</a>" : <i>[ &lt;a href=&#34;servicediscovery.md&#34;&gt;ServiceDiscovery&lt;/a&gt;, ... ]</i>,
        "<a href="#virtualservice" title="VirtualService">VirtualService</a>" : <i>[ &lt;a href=&#34;virtualservice.md&#34;&gt;VirtualService&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ &lt;a href=&#34;healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;, ... ]</i>,
        "<a href="#portmapping" title="PortMapping">PortMapping</a>" : <i>[ &lt;a href=&#34;portmapping.md&#34;&gt;PortMapping&lt;/a&gt;, ... ]</i>,
        "<a href="#accesslog" title="AccessLog">AccessLog</a>" : <i>[ &lt;a href=&#34;accesslog.md&#34;&gt;AccessLog&lt;/a&gt;, ... ]</i>,
        "<a href="#awscloudmap" title="AwsCloudMap">AwsCloudMap</a>" : <i>[ &lt;a href=&#34;awscloudmap.md&#34;&gt;AwsCloudMap&lt;/a&gt;, ... ]</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ &lt;a href=&#34;dns.md&#34;&gt;Dns&lt;/a&gt;, ... ]</i>,
        "<a href="#file" title="File">File</a>" : <i>[ &lt;a href=&#34;file.md&#34;&gt;File&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppmeshVirtualNode
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#meshname" title="MeshName">MeshName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;</i>
    <a href="#listener" title="Listener">Listener</a>: <i>
      - &lt;a href=&#34;listener.md&#34;&gt;Listener&lt;/a&gt;</i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;</i>
    <a href="#servicediscovery" title="ServiceDiscovery">ServiceDiscovery</a>: <i>
      - &lt;a href=&#34;servicediscovery.md&#34;&gt;ServiceDiscovery&lt;/a&gt;</i>
    <a href="#virtualservice" title="VirtualService">VirtualService</a>: <i>
      - &lt;a href=&#34;virtualservice.md&#34;&gt;VirtualService&lt;/a&gt;</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - &lt;a href=&#34;healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;</i>
    <a href="#portmapping" title="PortMapping">PortMapping</a>: <i>
      - &lt;a href=&#34;portmapping.md&#34;&gt;PortMapping&lt;/a&gt;</i>
    <a href="#accesslog" title="AccessLog">AccessLog</a>: <i>
      - &lt;a href=&#34;accesslog.md&#34;&gt;AccessLog&lt;/a&gt;</i>
    <a href="#awscloudmap" title="AwsCloudMap">AwsCloudMap</a>: <i>
      - &lt;a href=&#34;awscloudmap.md&#34;&gt;AwsCloudMap&lt;/a&gt;</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - &lt;a href=&#34;dns.md&#34;&gt;Dns&lt;/a&gt;</i>
    <a href="#file" title="File">File</a>: <i>
      - &lt;a href=&#34;file.md&#34;&gt;File&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No

_Type_: List of &lt;a href=&#34;listener.md&#34;&gt;Listener&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDiscovery

_Required_: No

_Type_: List of &lt;a href=&#34;servicediscovery.md&#34;&gt;ServiceDiscovery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualService

_Required_: No

_Type_: List of &lt;a href=&#34;virtualservice.md&#34;&gt;VirtualService&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheck.md&#34;&gt;HealthCheck&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMapping

_Required_: No

_Type_: List of &lt;a href=&#34;portmapping.md&#34;&gt;PortMapping&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLog

_Required_: No

_Type_: List of &lt;a href=&#34;accesslog.md&#34;&gt;AccessLog&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCloudMap

_Required_: No

_Type_: List of &lt;a href=&#34;awscloudmap.md&#34;&gt;AwsCloudMap&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of &lt;a href=&#34;dns.md&#34;&gt;Dns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### File

_Required_: No

_Type_: List of &lt;a href=&#34;file.md&#34;&gt;File&lt;/a&gt;

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

#### CreatedDate

Returns the &lt;code&gt;CreatedDate&lt;/code&gt; value.

#### LastUpdatedDate

Returns the &lt;code&gt;LastUpdatedDate&lt;/code&gt; value.

