# Terraform::AWS::OpsworksApplication

CloudFormation equivalent of aws_opsworks_application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::OpsworksApplication",
    "Properties" : {
        "<a href="#autobundleondeploy" title="AutoBundleOnDeploy">AutoBundleOnDeploy</a>" : <i>String</i>,
        "<a href="#awsflowrubysettings" title="AwsFlowRubySettings">AwsFlowRubySettings</a>" : <i>String</i>,
        "<a href="#datasourcearn" title="DataSourceArn">DataSourceArn</a>" : <i>String</i>,
        "<a href="#datasourcedatabasename" title="DataSourceDatabaseName">DataSourceDatabaseName</a>" : <i>String</i>,
        "<a href="#datasourcetype" title="DataSourceType">DataSourceType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#documentroot" title="DocumentRoot">DocumentRoot</a>" : <i>String</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#enablessl" title="EnableSsl">EnableSsl</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#railsenv" title="RailsEnv">RailsEnv</a>" : <i>String</i>,
        "<a href="#shortname" title="ShortName">ShortName</a>" : <i>String</i>,
        "<a href="#stackid" title="StackId">StackId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#appsource" title="AppSource">AppSource</a>" : <i>[ <a href="appsource.md">AppSource</a>, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environment.md">Environment</a>, ... ]</i>,
        "<a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>" : <i>[ <a href="sslconfiguration.md">SslConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::OpsworksApplication
Properties:
    <a href="#autobundleondeploy" title="AutoBundleOnDeploy">AutoBundleOnDeploy</a>: <i>String</i>
    <a href="#awsflowrubysettings" title="AwsFlowRubySettings">AwsFlowRubySettings</a>: <i>String</i>
    <a href="#datasourcearn" title="DataSourceArn">DataSourceArn</a>: <i>String</i>
    <a href="#datasourcedatabasename" title="DataSourceDatabaseName">DataSourceDatabaseName</a>: <i>String</i>
    <a href="#datasourcetype" title="DataSourceType">DataSourceType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#documentroot" title="DocumentRoot">DocumentRoot</a>: <i>String</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#enablessl" title="EnableSsl">EnableSsl</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#railsenv" title="RailsEnv">RailsEnv</a>: <i>String</i>
    <a href="#shortname" title="ShortName">ShortName</a>: <i>String</i>
    <a href="#stackid" title="StackId">StackId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#appsource" title="AppSource">AppSource</a>: <i>
      - <a href="appsource.md">AppSource</a></i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environment.md">Environment</a></i>
    <a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>: <i>
      - <a href="sslconfiguration.md">SslConfiguration</a></i>
</pre>

## Properties

#### AutoBundleOnDeploy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsFlowRubySettings

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSourceArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSourceDatabaseName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentRoot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSsl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RailsEnv

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSource

_Required_: No

_Type_: List of <a href="appsource.md">AppSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of <a href="environment.md">Environment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslConfiguration

_Required_: No

_Type_: List of <a href="sslconfiguration.md">SslConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

