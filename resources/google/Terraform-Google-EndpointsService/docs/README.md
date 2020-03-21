# Terraform::Google::EndpointsService

CloudFormation equivalent of google_endpoints_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::EndpointsService",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apis" title="Apis">Apis</a>" : <i>[ &lt;a href=&#34;apis.md&#34;&gt;Apis&lt;/a&gt;, ... ]</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>String</i>,
        "<a href="#dnsaddress" title="DnsAddress">DnsAddress</a>" : <i>String</i>,
        "<a href="#endpoints" title="Endpoints">Endpoints</a>" : <i>[ &lt;a href=&#34;endpoints.md&#34;&gt;Endpoints&lt;/a&gt;, ... ]</i>,
        "<a href="#grpcconfig" title="GrpcConfig">GrpcConfig</a>" : <i>String</i>,
        "<a href="#openapiconfig" title="OpenapiConfig">OpenapiConfig</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#protocoutputbase64" title="ProtocOutputBase64">ProtocOutputBase64</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::EndpointsService
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apis" title="Apis">Apis</a>: <i>
      - &lt;a href=&#34;apis.md&#34;&gt;Apis&lt;/a&gt;</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>String</i>
    <a href="#dnsaddress" title="DnsAddress">DnsAddress</a>: <i>String</i>
    <a href="#endpoints" title="Endpoints">Endpoints</a>: <i>
      - &lt;a href=&#34;endpoints.md&#34;&gt;Endpoints&lt;/a&gt;</i>
    <a href="#grpcconfig" title="GrpcConfig">GrpcConfig</a>: <i>String</i>
    <a href="#openapiconfig" title="OpenapiConfig">OpenapiConfig</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#protocoutputbase64" title="ProtocOutputBase64">ProtocOutputBase64</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Apis

_Required_: No

_Type_: List of &lt;a href=&#34;apis.md&#34;&gt;Apis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoints

_Required_: No

_Type_: List of &lt;a href=&#34;endpoints.md&#34;&gt;Endpoints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrpcConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenapiConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocOutputBase64

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Apis

Returns the &lt;code&gt;Apis&lt;/code&gt; value.

#### ConfigId

Returns the &lt;code&gt;ConfigId&lt;/code&gt; value.

#### DnsAddress

Returns the &lt;code&gt;DnsAddress&lt;/code&gt; value.

#### Endpoints

Returns the &lt;code&gt;Endpoints&lt;/code&gt; value.

