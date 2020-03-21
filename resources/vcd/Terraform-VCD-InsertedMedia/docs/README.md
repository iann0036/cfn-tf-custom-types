# Terraform::VCD::InsertedMedia

Provides a vCloud Director resource for inserting or ejecting media (ISO) file for the VM. Create this resource for inserting the media, and destroy it for ejecting.

Supported in provider *v2.0+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::InsertedMedia",
    "Properties" : {
        "<a href="#catalog" title="Catalog">Catalog</a>" : <i>String</i>,
        "<a href="#ejectforce" title="EjectForce">EjectForce</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#vappname" title="VappName">VappName</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#vmname" title="VmName">VmName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::InsertedMedia
Properties:
    <a href="#catalog" title="Catalog">Catalog</a>: <i>String</i>
    <a href="#ejectforce" title="EjectForce">EjectForce</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#vappname" title="VappName">VappName</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#vmname" title="VmName">VmName</a>: <i>String</i>
</pre>

## Properties

#### Catalog

The name of the catalog where to find media file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EjectForce

Allows to pass answer to question in vCD
"The guest operating system has locked the CD-ROM door and is probably using the CD-ROM.
Disconnect anyway (and override the lock)?"
when ejecting from a VM which is powered on. True means "Yes" as answer to question. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Media file name in catalog which will be inserted to VM.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappName

- The name of vApp to find.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmName

- The name of VM to be used to insert media file.

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

