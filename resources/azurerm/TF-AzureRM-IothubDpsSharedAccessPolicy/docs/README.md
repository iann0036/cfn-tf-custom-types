# TF::AzureRM::IothubDpsSharedAccessPolicy

Manages an IotHub Device Provisioning Service Shared Access Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::IothubDpsSharedAccessPolicy",
    "Properties" : {
        "<a href="#enrollmentread" title="EnrollmentRead">EnrollmentRead</a>" : <i>Boolean</i>,
        "<a href="#enrollmentwrite" title="EnrollmentWrite">EnrollmentWrite</a>" : <i>Boolean</i>,
        "<a href="#iothubdpsname" title="IothubDpsName">IothubDpsName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#registrationread" title="RegistrationRead">RegistrationRead</a>" : <i>Boolean</i>,
        "<a href="#registrationwrite" title="RegistrationWrite">RegistrationWrite</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#serviceconfig" title="ServiceConfig">ServiceConfig</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::IothubDpsSharedAccessPolicy
Properties:
    <a href="#enrollmentread" title="EnrollmentRead">EnrollmentRead</a>: <i>Boolean</i>
    <a href="#enrollmentwrite" title="EnrollmentWrite">EnrollmentWrite</a>: <i>Boolean</i>
    <a href="#iothubdpsname" title="IothubDpsName">IothubDpsName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#registrationread" title="RegistrationRead">RegistrationRead</a>: <i>Boolean</i>
    <a href="#registrationwrite" title="RegistrationWrite">RegistrationWrite</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#serviceconfig" title="ServiceConfig">ServiceConfig</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### EnrollmentRead

Adds `EnrollmentRead` permission to this Shared Access Account. It allows read access to enrollment data.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnrollmentWrite

Adds `EnrollmentWrite` permission to this Shared Access Account. It allows write access to enrollment data.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IothubDpsName

The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistrationRead

Adds `RegistrationStatusRead` permission to this Shared Access Account. It allows read access to device registrations.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistrationWrite

Adds `RegistrationStatusWrite` permission to this Shared Access Account. It allows write access to device registrations.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConfig

Adds `ServiceConfig` permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### PrimaryConnectionString

Returns the <code>PrimaryConnectionString</code> value.

#### PrimaryKey

Returns the <code>PrimaryKey</code> value.

#### SecondaryConnectionString

Returns the <code>SecondaryConnectionString</code> value.

#### SecondaryKey

Returns the <code>SecondaryKey</code> value.

