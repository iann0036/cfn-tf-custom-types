# TF::Alicloud::EdasApplication

Creates an EDAS ecs application on EDAS. The application will be deployed when `group_id` and `war_url` are given.

-> **NOTE:** Available in 1.82.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EdasApplication",
    "Properties" : {
        "<a href="#applicationname" title="ApplicationName">ApplicationName</a>" : <i>String</i>,
        "<a href="#buildpackid" title="BuildPackId">BuildPackId</a>" : <i>Double</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#descriotion" title="Descriotion">Descriotion</a>" : <i>String</i>,
        "<a href="#ecuinfo" title="EcuInfo">EcuInfo</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#healthcheckurl" title="HealthCheckUrl">HealthCheckUrl</a>" : <i>String</i>,
        "<a href="#logicalregionid" title="LogicalRegionId">LogicalRegionId</a>" : <i>String</i>,
        "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
        "<a href="#packageversion" title="PackageVersion">PackageVersion</a>" : <i>String</i>,
        "<a href="#warurl" title="WarUrl">WarUrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EdasApplication
Properties:
    <a href="#applicationname" title="ApplicationName">ApplicationName</a>: <i>String</i>
    <a href="#buildpackid" title="BuildPackId">BuildPackId</a>: <i>Double</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#descriotion" title="Descriotion">Descriotion</a>: <i>String</i>
    <a href="#ecuinfo" title="EcuInfo">EcuInfo</a>: <i>
      - String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#healthcheckurl" title="HealthCheckUrl">HealthCheckUrl</a>: <i>String</i>
    <a href="#logicalregionid" title="LogicalRegionId">LogicalRegionId</a>: <i>String</i>
    <a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
    <a href="#packageversion" title="PackageVersion">PackageVersion</a>: <i>String</i>
    <a href="#warurl" title="WarUrl">WarUrl</a>: <i>String</i>
</pre>

## Properties

#### ApplicationName

Name of your EDAS application. Only letters '-' '_' and numbers are allowed. The length cannot exceed 36 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildPackId

The package ID of Enterprise Distributed Application Service (EDAS) Container, which can be retrieved by calling container version list interface ListBuildPack or the "Pack ID" column in container version list. When creating High-speed Service Framework (HSF) application, this parameter is required.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

The ID of the cluster that you want to create the application. The default cluster will be used if you do not specify this parameter.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Descriotion

The description of the application that you want to create.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcuInfo

The ID of the Elastic Compute Unit (ECU) where you want to deploy the application. Type: List.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The ID of the instance group where the application is going to be deployed. Set this parameter to all if you want to deploy the application to all groups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUrl

The URL for health checking of the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalRegionId

The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

The type of the package for the deployment of the application that you want to create. The valid values are: WAR and JAR. We strongly recommend you to set this parameter when creating the application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageVersion

The version of the application that you want to deploy. It must be unique for every application. The length cannot exceed 64 characters. We recommended you to use a timestamp.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarUrl

The address to store the uploaded web application (WAR) package for application deployment. This parameter is required when the deployType parameter is set as url.

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

#### Id

Returns the <code>Id</code> value.

