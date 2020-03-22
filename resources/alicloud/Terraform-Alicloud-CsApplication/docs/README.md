# Terraform::Alicloud::CsApplication

-> **DEPRECATED:** This resource manages applications in swarm cluster only, which is being deprecated and will be replaced by Kubernetes cluster.

This resource use an orchestration template to define and deploy a multi-container application. An application is created by using an orchestration template.
Each application can contain one or more services.

-> **NOTE:** Application orchestration template must be a valid Docker Compose YAML template.

-> **NOTE:** At present, this resource only support swarm cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CsApplication",
    "Properties" : {
        "<a href="#bluegreen" title="BlueGreen">BlueGreen</a>" : <i>Boolean</i>,
        "<a href="#bluegreenconfirm" title="BlueGreenConfirm">BlueGreenConfirm</a>" : <i>Boolean</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environment.md">Environment</a>, ... ]</i>,
        "<a href="#latestimage" title="LatestImage">LatestImage</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CsApplication
Properties:
    <a href="#bluegreen" title="BlueGreen">BlueGreen</a>: <i>Boolean</i>
    <a href="#bluegreenconfirm" title="BlueGreenConfirm">BlueGreenConfirm</a>: <i>Boolean</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environment.md">Environment</a></i>
    <a href="#latestimage" title="LatestImage">LatestImage</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### BlueGreen

Wherther to use "Blue Green" method when release a new version. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueGreenConfirm

Whether to confirm a "Blue Green" application. Default to false. It will be ignored when `blue_green` is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

The swarm cluster's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

A key/value map used to replace the variable parameter in the Compose template.

_Required_: No

_Type_: List of <a href="environment.md">Environment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatestImage

Whether to use latest docker image while each updating application. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The application deployment template and it must be [Docker Compose format](https://docs.docker.com/compose/).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The application deploying version. Each updating, it must be different with current. Default to "1.0".

_Required_: No

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

#### DefaultDomain

Returns the <code>DefaultDomain</code> value.

#### Id

Returns the <code>Id</code> value.

#### Services

Returns the <code>Services</code> value.

