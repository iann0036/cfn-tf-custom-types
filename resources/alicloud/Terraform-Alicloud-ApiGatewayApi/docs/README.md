# Terraform::Alicloud::ApiGatewayApi

CloudFormation equivalent of alicloud_api_gateway_api

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::ApiGatewayApi",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>String</i>,
        "<a href="#stagenames" title="StageNames">StageNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#constantparameters" title="ConstantParameters">ConstantParameters</a>" : <i>[ &lt;a href=&#34;constantparameters.md&#34;&gt;ConstantParameters&lt;/a&gt;, ... ]</i>,
        "<a href="#fcserviceconfig" title="FcServiceConfig">FcServiceConfig</a>" : <i>[ &lt;a href=&#34;fcserviceconfig.md&#34;&gt;FcServiceConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#httpserviceconfig" title="HttpServiceConfig">HttpServiceConfig</a>" : <i>[ &lt;a href=&#34;httpserviceconfig.md&#34;&gt;HttpServiceConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#httpvpcserviceconfig" title="HttpVpcServiceConfig">HttpVpcServiceConfig</a>" : <i>[ &lt;a href=&#34;httpvpcserviceconfig.md&#34;&gt;HttpVpcServiceConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#mockserviceconfig" title="MockServiceConfig">MockServiceConfig</a>" : <i>[ &lt;a href=&#34;mockserviceconfig.md&#34;&gt;MockServiceConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#requestconfig" title="RequestConfig">RequestConfig</a>" : <i>[ &lt;a href=&#34;requestconfig.md&#34;&gt;RequestConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ &lt;a href=&#34;requestparameters.md&#34;&gt;RequestParameters&lt;/a&gt;, ... ]</i>,
        "<a href="#systemparameters" title="SystemParameters">SystemParameters</a>" : <i>[ &lt;a href=&#34;systemparameters.md&#34;&gt;SystemParameters&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::ApiGatewayApi
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicetype" title="ServiceType">ServiceType</a>: <i>String</i>
    <a href="#stagenames" title="StageNames">StageNames</a>: <i>
      - String</i>
    <a href="#constantparameters" title="ConstantParameters">ConstantParameters</a>: <i>
      - &lt;a href=&#34;constantparameters.md&#34;&gt;ConstantParameters&lt;/a&gt;</i>
    <a href="#fcserviceconfig" title="FcServiceConfig">FcServiceConfig</a>: <i>
      - &lt;a href=&#34;fcserviceconfig.md&#34;&gt;FcServiceConfig&lt;/a&gt;</i>
    <a href="#httpserviceconfig" title="HttpServiceConfig">HttpServiceConfig</a>: <i>
      - &lt;a href=&#34;httpserviceconfig.md&#34;&gt;HttpServiceConfig&lt;/a&gt;</i>
    <a href="#httpvpcserviceconfig" title="HttpVpcServiceConfig">HttpVpcServiceConfig</a>: <i>
      - &lt;a href=&#34;httpvpcserviceconfig.md&#34;&gt;HttpVpcServiceConfig&lt;/a&gt;</i>
    <a href="#mockserviceconfig" title="MockServiceConfig">MockServiceConfig</a>: <i>
      - &lt;a href=&#34;mockserviceconfig.md&#34;&gt;MockServiceConfig&lt;/a&gt;</i>
    <a href="#requestconfig" title="RequestConfig">RequestConfig</a>: <i>
      - &lt;a href=&#34;requestconfig.md&#34;&gt;RequestConfig&lt;/a&gt;</i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - &lt;a href=&#34;requestparameters.md&#34;&gt;RequestParameters&lt;/a&gt;</i>
    <a href="#systemparameters" title="SystemParameters">SystemParameters</a>: <i>
      - &lt;a href=&#34;systemparameters.md&#34;&gt;SystemParameters&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConstantParameters

_Required_: No

_Type_: List of &lt;a href=&#34;constantparameters.md&#34;&gt;ConstantParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FcServiceConfig

_Required_: No

_Type_: List of &lt;a href=&#34;fcserviceconfig.md&#34;&gt;FcServiceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServiceConfig

_Required_: No

_Type_: List of &lt;a href=&#34;httpserviceconfig.md&#34;&gt;HttpServiceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpVpcServiceConfig

_Required_: No

_Type_: List of &lt;a href=&#34;httpvpcserviceconfig.md&#34;&gt;HttpVpcServiceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MockServiceConfig

_Required_: No

_Type_: List of &lt;a href=&#34;mockserviceconfig.md&#34;&gt;MockServiceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestConfig

_Required_: No

_Type_: List of &lt;a href=&#34;requestconfig.md&#34;&gt;RequestConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

_Required_: No

_Type_: List of &lt;a href=&#34;requestparameters.md&#34;&gt;RequestParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemParameters

_Required_: No

_Type_: List of &lt;a href=&#34;systemparameters.md&#34;&gt;SystemParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiId

Returns the &lt;code&gt;ApiId&lt;/code&gt; value.

